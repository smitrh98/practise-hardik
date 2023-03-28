# 3. Write a Python program to subtract five days from the current date.
from datetime import timedelta,datetime
x=datetime.now()
print(x)
y=timedelta(days=5)
print(y)
z=x-y
print(z)