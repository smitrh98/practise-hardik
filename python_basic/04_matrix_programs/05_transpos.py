# Transpose a matrix in Single line in Python
li=[[1,2,3],
    [4,5,6],
    [7,8,9]]
#1
new_li=[]
for i in range(len(li)):
    x=[]
    for j in range(len(li[i])):
        x.append(li[j][i])
    new_li.append(x)
print(new_li)
#2
n_li=[[li[j][i] for j in range(len(li[i]))] for i in range(len(li))]
print(n_li)

