def fib_nmult(n,num):
    a=0
    b=1
    i=0
    while True:
        temp=a
        a=b
        b=b+temp
        if temp%num==0:
            # print(temp) #excluding 0.
            if i==n:
                print(temp)
                break
            i+=1
fib_nmult(5,3)
 