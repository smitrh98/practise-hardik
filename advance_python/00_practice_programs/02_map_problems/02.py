# 2. Write a Python program to listify the list of given strings individually using 
# Python map.  Original list: ['Red', 'Blue', 'Black', 'White', ‘Pink’]. 
# Result List : [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
list1=['Red', 'Blue', 'Black', 'White', 'Pink']
final_list=list(map(lambda x:list(x),list1))
print(final_list)

