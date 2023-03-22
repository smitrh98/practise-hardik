# Python – Join Tuples if similar initial element
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
li=[(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
n_li=[]
for i in li:
    n_li.append(list(i))
print(n_li)
i=0
while i<len(n_li)-1:
    if n_li[i][0]==n_li[i+1][0]:
        n_li[i].append(n_li[i+1][1])
        n_li.pop(i+1)
        i=i
    else:
        i+=1
print(n_li)   #?????????


