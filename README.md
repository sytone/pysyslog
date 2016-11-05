# pysyslog

Tiny Syslog Server in Python.

This is a tiny syslog server that is able to receive UDP based syslog entries on a specified port and save them to a file.

That's it... it does nothing else...

Basic Usage: 
  python pysyslog.py

Command line switches are optional. The following switches are recognized.

    -l <logfile>      -- Specify the log file to write to. Default is pysyslog.log
    -p <port>         -- Specify the port to listen on. Default is 514
    -i <boundip>      -- Specify the IP address to listen on. Default is 0.0.0.0

## Example
This will start the process listening on port 514 bound to all IP addreses  and writing to EspEasy.log
     
     pysyslog.py -l EspEasy.log

