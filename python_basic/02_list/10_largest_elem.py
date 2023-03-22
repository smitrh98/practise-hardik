# Python program to find largest number in a list
li=[23,45,67,89,12,34,56,78]
max=li[0]
for i in li:
    if i>max:
        max=i
print(f"Max : {max}")