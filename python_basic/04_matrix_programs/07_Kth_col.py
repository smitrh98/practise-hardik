# Python | Get Kth Column of Matrix
m=[[1,2,3],
   [4,5,6],
   [7,8,9],
   [10,11,12]]
col=2
li=[]
for i in range(len(m)):
    li.append(m[i][col-1])
print(li)


