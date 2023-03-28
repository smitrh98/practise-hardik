# 2. Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00
from datetime import datetime 
string_time='Mon Jan 1 2014 2:43PM'
format='%a %b %d %Y %I:%M%p'
x=datetime.strptime(string_time,format)
print(x)

string_time='Sun January 1 2023 5:56PM GMT'
format='%a %B %d %Y %I:%M%p %Z'
x=datetime.strptime(string_time,format)
print(x)
print(x.strftime('%d/%m/%Y %H:%M:%S'))