# Python program to add two Matrices
a=[[1,2,3],
   [1,2,4,5],
   [7,8,9]]
b=[[9,8,7],
   [1,3,1,5],
   [3,2,2]]
sum=a[:][:]
for i in range(len(a)):
    for j in range(len(a)):
        sum[i][j]=a[i][j]+b[i][j]        
print(sum)

# a=[[1,2,3,3],
#    [1,2,4,4],
#    [7,8,9,3]]
# b=[[9,8,7,3],
#    [1,3,1,4],
#    [3,2,2,3]]
# c=[]
   
# for i in range(len(a)):
#    sum=[]
#    for j in range(len(a[i])):
#       x=a[i][j]+b[i][j]
#       sum.append(x)
#    c.append(sum)
# print(c)   
 