# Python – All pair combinations of 2 tuples
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8) 
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
t1 = (7, 2)
t2 = (7, 8)
li=[]
for i in range(len(t1)):
    for j in range(len(t2)):
        x=tuple([t1[i],t2[j]])
        y=tuple([t2[i],t1[j]])
        li.append(x)
        li.append(y)
print(li)
