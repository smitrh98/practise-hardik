# Python – Remove Tuples of Length K
# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2 
# Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
# Explanation : (4, 5) of len = 2 is removed.
li = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k=2
for i in li:
    if len(i)==k:
        print(i,"is removed.")
        li.remove(i)
print(li)
