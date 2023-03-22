# Different ways to clear a list in Python
#1
li=[23,45,67,89,12,34,56,78]
li.clear()
print(li)
#2
li=[23,45,67,89,12,34,56,78]
li[:]=[]
print(li)
#3
li=[23,45,67,89,12,34,56,78]
del li[:]
print(li)
