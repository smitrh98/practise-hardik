# Python | Ways to check if element exists in list
li=[23,45,67,89,12,34,56,78]
#1
print(li.index(45))
#it give ValueError if element not in li.
#2
x=44
for i in li:
    if x==i:
        print(f"{x} Element is in list.") 
        break
else:
    print(f"{x} Element is not in list.") 
