# 2.Find the factorial of a number 
import math
a='y'
while(a=='y' or a=='Y'):
    x=int(input("Enter integer number : "))
    y=math.factorial(x)
    print(y)
    a=input('If you want to continue enter "y" or "Y":')