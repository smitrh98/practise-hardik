# Ways to remove i’th character from string in Python
def new_remove(s,pos):
    s2=s[:pos-1]+s[pos:]
    print(s2)
def remove(s,pos): #repetation not allow in this case
    print(s)
    s1=s.replace(s[pos-1],"",1)
    print(s1)
str1='GeeksforGeeks'
pos=11
remove(str1,pos)
new_remove(str1,pos)



