# Python program to interchange first and last elements in a list
li=["Hardik","Parmar","LDCE"]
temp=li[0]
li[0]=li[-1]
li[-1]=temp
print(li)