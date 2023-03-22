def cube_sum(n):
    sum=0
    for i in range(1,n+1):
        print(i**3)
        sum=sum+i**3
    print(sum)
cube_sum(10)