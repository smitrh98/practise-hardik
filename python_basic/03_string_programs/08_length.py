# Find length of a string in python (4 ways)
#1
s1="Nividata Consultancy"
print(len(s1))
#2
len=0
for i in s1:
    len+=1
print(len)
#3
len=0
while s1[len:]:
    len+=1
print(len)
#4

