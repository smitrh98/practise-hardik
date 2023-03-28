# 2. Implement a logger which would log into a separate file for debug, info ,
# warning, error level logs
from logging import *
LOG_FORMAT='{lineno} -- {name} -- {levelname} -- {msg} -- {asctime}'
basicConfig(filename="my_logfile.log",level=DEBUG,format=LOG_FORMAT,style="{")
debug("This is DEBUG  logging message.")
info("This is INFO logging message.")
warning("This is WARNING logging message.")
error("This is ERROR logging message.")
critical("This is CRITICAL logging message.")