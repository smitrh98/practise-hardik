# Python – Maximum and Minimum K elements in Tuple
test_tup = (5, 20, 3, 7, 6, 8)
k=2
li=list(test_tup)
li.sort()
print(li)
li.remove(li[1])
li.remove(li[len(li)-1-2])
print(tuple(li))