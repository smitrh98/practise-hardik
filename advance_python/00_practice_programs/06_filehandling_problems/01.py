# 1.Write a Python program to read an entire text file.
#1
f=open('my_file.txt','r')
print(f.read())
f.close()
#2 #here we don't need to close the file it close after exicution of code.
with open('my_file.txt','r') as f:
    x=f.read()
    print(x)
