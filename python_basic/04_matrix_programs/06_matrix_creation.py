# Python | Matrix creation of n*n
n=4
n_li=[]
for i in range(n):
    li=list(range(1+n*i,1+n*(i+1)))
    n_li.append(li)
print(n_li)