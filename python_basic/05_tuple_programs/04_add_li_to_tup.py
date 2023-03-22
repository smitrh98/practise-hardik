# Python – Adding Tuple to List and vice – versa
tup=(2,3,4,5,6,7,8)
li=[1,2,3,4,5,6,7,8,9,10]
#1
li.extend(tup)
print(li)
#2
tup=(2,3,4,5,6,7,8)
li=[1,2,3,4,5,6,7,8,9,10]
t_final=tup+tuple(li)
print(t_final)