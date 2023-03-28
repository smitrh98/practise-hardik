# 5. Write a Python program to convert a given list of tuples to a list of strings 
#using the map and join function 
#Original list of tuples: [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
# Result list: ['red pink', 'white black', 'orange green']
List1=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
Final_List=list(map(lambda x:" ".join(x),List1))
print(Final_List)

