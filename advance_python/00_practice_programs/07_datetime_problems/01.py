# 1. Write a Python script to display the various Date Time formats
from time import time,ctime,localtime
from datetime import datetime
# a) Current date and time
x=ctime()
print("Current Date and Time : ",x)
# z=datetime.now()
# a=z.strftime('%d/%m/%Y %H:%M:%S')
# print(a)
# b) Current year
y=localtime()
print("Current year ",y.tm_year)
# c) Month of year
print("Month of year ",y.tm_mon)
# d) Week number of the year
z=datetime.now()
print("Week number of the year ",z.isocalendar().week)
# e) Weekday of the week
print("Weekday of the week ",y.tm_wday)
# f) Day of year
print("Day of year ",y.tm_yday)
# g) Day of the month
print("Day of the month",y.tm_mday)
# h) Day of week
print("Day of week",y.tm_wday)

