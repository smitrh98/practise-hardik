a=[[1,1,1],
   [2,2,2],
   [3,3,3]]
b=[[1,1,1],
   [2,2,2],
   [3,3,3]]
ans=[]
for i in range(len(a)):
    x=[]
    for j in range(len(a[0])):
        sum=0
        for k in range(len(a[0])):
            sum=sum+a[i][k]*b[k][j]
        x.append(sum)
    ans.append(x)
print(ans)    
