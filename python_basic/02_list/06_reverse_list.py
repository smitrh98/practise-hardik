# Python | Reversing a List
#1
li=[23,45,67,89,12,34,56,78]
li.reverse()
print(li)
#2
li=[23,45,67,89,12,34,56,78]
new_li=[]
for i in range(len(li)):
    new_li.append(li[len(li)-1-i])
print(new_li)
#3
li=[23,45,67,89,15,12,34,56,78]
for i in range(int(len(li)/2)):
    temp=li[i]
    li[i]=li[len(li)-i-1]
    li[len(li)-i-1]=temp
print(li)
