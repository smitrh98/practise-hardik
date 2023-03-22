# Python program to print even length words in a string
s="Hii , I am Hardik from Bhavnagar."
x=s.split()
for i in x:
    if len(i)%2==0:
        print(i,end=" ")

    