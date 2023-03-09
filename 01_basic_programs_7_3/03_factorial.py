def fact(x):
    if x<0:
        return "You enter Invalid Number."
    elif x == 0:
        fact=1
    else:
        fact=1
        for i in range(1,x+1):
            fact=fact*i
    return fact
x=-1
print(fact(x))