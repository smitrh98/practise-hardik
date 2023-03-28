# 3. Implement a logger which would log into a separate file with variable data for
# log strings for debug, info , warning, error level logs
from logging import *
LOG_FORMAT='%(lineno)2d -- %(name)s -- %(levelname)8s-- %(asctime)s -- %(msg)s '
basicConfig(filename="my_logfile2.log",level=DEBUG,format=LOG_FORMAT)
debug("{x} This is DEBUG  logging message. {y}".format(x="Hardik,",y="For you.."))
info("This is INFO logging message.")
warning("This is WARNING logging message.")
error("This is ERROR logging message.")
critical("This is CRITICAL logging message.")