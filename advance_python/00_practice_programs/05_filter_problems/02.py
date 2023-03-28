# 2.Filter the list by both odd and even numbers separate list from the sequence. 
# seq = [0, 1, 2, 3, 5, 8, 13, 15, 16, 17, 22, 14]
seq = [0, 1, 2, 3, 5, 8, 13, 15, 16, 17, 22, 14]
even=list(filter(lambda x:x%2==0,seq))
print(even)
odd=list(filter(lambda x:x%2!=0,seq))
print(odd)