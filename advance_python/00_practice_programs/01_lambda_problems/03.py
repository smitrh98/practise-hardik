# Write a Python program to filter a list of integers using Lambda.   
#Original list of integers:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Even numbers from the said list:[2, 4, 6, 8, 10] 
# Odd numbers from the said list:[1, 3, 5, 7, 9] 
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
l2=list(filter(lambda x:x%2==0,l1))
print(l2)
l3=list(filter(lambda x:x%2!=0,l1))
print(l3)