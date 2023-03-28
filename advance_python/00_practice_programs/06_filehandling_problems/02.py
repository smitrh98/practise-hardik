# 2. Write a Python program to read first n lines of a file.
file=open('my_file.txt','r')
n=4
for i in range(n):
    print(file.readline())
file.close()
