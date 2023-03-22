# Python – Words Frequency in String Shorthands
str1="Hardik Parmar LDCE Hardik"
#1
x=str1.split()
y=0
di=dict.fromkeys(x,y)
for i in x:
    di[i]+=1
print(di)
#2
x=str1.split()
s=set(x)
for i in s:
    print([i,x.count(i)])