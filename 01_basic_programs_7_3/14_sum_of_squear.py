def sum_square(n):
    sum=0
    for i in range(1,n+1):
        print(i**2)
        sum=sum+i**2
    print(sum)
sum_square(15)