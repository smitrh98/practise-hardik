# 3. Filter list elements starting with given Prefix “s”. 
# test_list = ['sapple', 'orange', 'smango', 'grape']
test_list = ['sapple', 'orange', 'smango', 'grape']
my_list=list(filter(lambda x:x.startswith('s'),test_list))
print(my_list)