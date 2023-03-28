#1.	Write a Python program to triple all numbers in a given list of integers. 
#Use Python map. Original list:  [1, 2, 3, 4, 5, 6, 7] 
#Result List: [3, 6, 9, 12, 15, 18, 21]
original_list=[1, 2, 3, 4, 5, 6, 7]
result_list=list(map(lambda x:x*3,original_list))
print(result_list)