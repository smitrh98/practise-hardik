def prime_num(n):
    if n<=0:
        print("Enter positive number.")
    elif n==1:
        print('1 is not a Prime Number.')
    else:
        y=0
        for i in range(2,n):
            if n%i==0:
                y=y+1
        if y==0:
            print(f"{n} is a Prime Number.")
        else:
            print(f"{n} is not a Prime Number.")
prime_num(20)