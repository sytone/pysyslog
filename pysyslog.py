#!/usr/bin/env python
"""
Tiny Syslog Server in Python.

This is a tiny syslog server that is able to receive UDP based syslog
entries on a specified port and save them to a file.
That's it... it does nothing else...
There are a few configuration parameters.
"""
import logging
import socketserver
import sys
import getopt


## These are the defaults.
LOG_FILE = 'pysyslog.log'
BOUND_IP, PORT = "0.0.0.0", 514

def main(argv):
    """
    Main function to set up socket listener for supplied args
    """
    logfile = LOG_FILE
    boundip = BOUND_IP
    port = PORT
    try:
        opts, args = getopt.getopt(argv, "hl:p:i:", ["logfile=", "port=", "boundip="])
    except getopt.GetoptError:
        show_help()
    for opt, arg in opts:
        if opt == '-h':
            show_help()
            sys.exit()
        elif opt in ("-l", "--logfile"):
            logfile = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-i", "--boundip"):
            boundip = arg
    print('       Writing to: {}'.format(logfile))
    print('     Listening on: {}'.format(port))
    print('         Bound to: {}'.format(boundip))
    print('Ignored Arguments: {}'.format(args))
    print('')
    print('Starting Server, press Ctrl+C to shutdown.')
    print('')

    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='',
                        filename=logfile, filemode='a')

    try:
        server = socketserver.UDPServer((boundip, port), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("Crtl+C Pressed. Shutting down.")

def show_help():
    """
    Help message to display if bad arguments or help requested.
    """
    print('-------------------------------------------------------------------------------')
    print('Python base Syslog server')
    print(' This is a light weight syslog server which is good for ')
    print(' playing with IoT projects that use systlog like ESPEasy')
    print('Basic Usage: pysyslog.py')
    print('')
    print('Command line switches are optional. The following switches are recognized.')
    print(' -l <logfile>      -- Specify the log file to write to. Default is pysyslog.log')
    print(' -p <port>         -- Specify the port to listen on. Default is 514')
    print(' -i <boundip>      -- Specify the IP address to listen on. Default is 0.0.0.0')
    print('')
    print('Example:')
    print(' This will start the process listening on port 514 bound to all IP addreses')
    print('  and writing to EspEasy.log')
    print(' pysyslog.py -l EspEasy.log ')
    print('-------------------------------------------------------------------------------')
    sys.exit(2)


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    """
    The actual core of the script, this listens on the socket.
    """

    def handle(self):
        try:
            data = bytes.decode(self.request[0].strip(), encoding="utf-8")
        except UnicodeError:
            data = 'unkown packet contents'

        # socket = self.request[1]
        print("%s : " % self.client_address[0], str(data))
        logging.info(str(data))


if __name__ == "__main__":
    main(sys.argv[1:])


