# 5. Write a Python program to count the frequency of words in a file.
from collections import Counter
with open('my_file.txt','r') as f:
    x=f.read().split()
    di=Counter(x)
    print(di)
