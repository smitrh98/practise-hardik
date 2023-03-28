# 4. Given two lists of strings string and substr, write a Python program to filter out
# all the strings in string that contains string in substr. 
# Input : string = ['city1', 'class5', 'room2', 'city2']
# substr = ['class', 'city']
# Output : ['city1', 'class5', 'city2']

string = ['city1', 'class5', 'room2', 'city2']
substr = ['class', 'city']
#1
final_list=[i for i in string for j in substr if j==i[:len(j)]]
print(final_list)
#2
def Filter(x,y):
    li=[]
    for i in x:
        for j in y:
            if j==i[:len(j)]:
                li.append(i)
    print(li)
Filter(string,substr)
#3
def Filter(string,substr):
    return [str for str in string if any(sub in str for sub in substr)]
print(Filter(string,substr))

