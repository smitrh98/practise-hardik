# 4. Write a Python program to drop microseconds from datetime
from datetime import datetime,timedelta
#1
time=datetime.now().microsecond
print(time)
z=datetime.now()-timedelta(microseconds=time)
print(z)
#2
a=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(a)