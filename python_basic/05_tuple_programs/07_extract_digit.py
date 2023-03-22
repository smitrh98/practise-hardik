# Python – Extract digits from Tuple list
# Input : test_list = [(15, 3), (3, 9)] 
# Output : [9, 5, 3, 1]
li1 = [(15, 3), (3, 9)]
li2=[]
for i in range(len(li1)):
    for j in range(len(li1[i])):
        a=li1[i][j]
        while a>0:
            d=a%10
            a=a//10
            li2.append(d)
s=set(li2)
l_final=list(s)
print(l_final)
