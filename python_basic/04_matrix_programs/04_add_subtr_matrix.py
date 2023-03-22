# Adding and Subtracting Matrices in Python
a=[[1,1,1],[2,2,2,4],[3,3,3]]
b=[[3,3,3],[2,2,2,2],[1,1,1]]
ans=[]
for i in range(len(a)):
    x=[]
    for j in range(len(a[i])):
        sub=a[i][j]-b[i][j]
        x.append(sub)
    ans.append(x)
print(ans)
