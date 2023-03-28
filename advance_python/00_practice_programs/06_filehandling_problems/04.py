# 4. Write a python program to find the longest words.
import functools
with open('my_file.txt','r') as file:
    d=file.read()
    print(d,end='\n\n')
    
    li=d.split()
    x=0
    for i in range(len(li)-1):
        if len(li[i])>x:
            x=len(li[i])
            max=li[i]
    print(f'Longest word in the file is --> "{max}"')





