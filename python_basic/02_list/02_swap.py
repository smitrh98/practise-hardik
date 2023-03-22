# Python program to swap two elements in a list
# if position is given
li=[23,45,67,89,12,34,56,78]
p1=3
p2=7
print(li)
temp=li[p1-1]
li[p1-1]=li[p2-1]
li[p2-1]=temp
print(li)
