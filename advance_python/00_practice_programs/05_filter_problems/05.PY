# 5. Print the selected values from a dictionary. 
# test_dict = {"Akash" : 1, "Akshat" : 2, "Nikhil" : 3, "Manjeet" : 4}
#  select_list = ['Manjeet', 'Nikhil']

test_dict = {"Akash" : 1, "Akshat" : 2, "Nikhil" : 3, "Manjeet" : 4}
select_list = ['Manjeet', 'Nikhil']
#1
final_list=[(y,test_dict[y]) for y in test_dict if y in select_list]
print(final_list)
#2
Filter= lambda x: True if x[0] in select_list else False
print(list(filter(Filter,test_dict.items())))
#3
def Filter(test_dict,select_list):
    li=[]
    for x,y in test_dict.items():
        if x in select_list:
            li.append((x,y))
    print(li)
Filter(test_dict,select_list)

