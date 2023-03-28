# 1.Implement a simple logger which prints the log message in console for 
# warning, info, error level logs
from logging import *
LOG_FORMAT="%(name)s--%(levelname)s--%(msg)s"
basicConfig(level=INFO,format=LOG_FORMAT)
info("This is info message of logging.")
warning("This is warning message of logging.")
error("This is error message of logging.")




