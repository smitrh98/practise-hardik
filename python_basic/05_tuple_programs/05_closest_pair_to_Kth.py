# Python – Closest Pair to Kth index element in Tuple
test_list = [(3, 4), (78, 76),(19, 23), (2, 3), (9, 8)] 
tup = (17, 23) 
k = 2
test_list = [(3, 4, 9), (5, 6, 7)] 
tup = (1, 2, 5) 
k = 3
d=abs(test_list[0][k-1]-tup[k-1])
x=0
for i in range(len(test_list)):
    if d> abs(test_list[i][k-1]-tup[k-1]):
        d=abs(test_list[i][k-1]-tup[k-1])
        x=i
print(test_list[x])