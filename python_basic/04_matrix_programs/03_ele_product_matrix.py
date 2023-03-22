# Python program for Matrix Product
a=[[1,2,3],[4],[5,6],[7,8,9,10]]
#1
ans=1
for i in range(len(a)):
    for j in range(len(a[i])):
        ans=ans*a[i][j]
print(ans)
#2
def product(li):
    ans=1
    for j in li:
        ans=ans*j
    return ans
print(product([j for i in a for j in i]))
#3
x=[]
for i in a:
    x.extend(i)
    ans=1
for j in x:
    ans*=j
print(ans)