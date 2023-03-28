# 5. Write a Python program to calculate the difference between two dates
from datetime import datetime,timedelta
x= datetime.now()
y=datetime(year=2020,month=4,day=23)
print(x-y)