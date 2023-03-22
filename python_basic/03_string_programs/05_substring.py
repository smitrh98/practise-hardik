# Python | Check if a Substring is Present in a Given String 
#1
s1="geeks for geeks"
sub_s1 = "geeks"
x=s1.split()
for i in x:
    if i==sub_s1:
        print(f"{sub_s1} is subString of {s1} .")
        break
    else:
        print("It is not.")
#2
s1="--H-Ha-Hardik-Harsh"
sub='Hardik'

if sub in s1:
    print("yes")
else:
    print("No")
    

