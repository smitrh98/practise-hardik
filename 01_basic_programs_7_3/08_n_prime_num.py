def prime_num_in_n(n):
    for i in range(2,n):
        x=0
        for j in range(2,i):
            if i%j==0:
                x+=1
        if x==0:
            print(i,end=",")

prime_num_in_n(100)
#we can add add start limit also but for that
#we have to use one more if loop to check (start>1)
