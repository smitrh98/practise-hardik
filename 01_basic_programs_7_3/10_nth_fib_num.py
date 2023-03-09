def n_fib(n):
    a=0
    b=1
    while n>0:
        # print(a,end=",") # this is for print all n num.
        temp=a
        a=b
        b=temp+b
        n-=1
    print(f"Nth Fib Number is {temp}.")
n_fib(10)
    