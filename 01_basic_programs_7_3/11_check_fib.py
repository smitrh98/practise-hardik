def check_fib(n):
    a=0
    b=1
    m=n
    while n>0:
        temp=a
        a=b
        b=temp+b
        if temp==m:
            print(f'{m} is Fibonacci number.')
            break
        elif temp>m:
            print(f'{m} is not Fibonacci number.')
            break
        n-=1
check_fib(89)