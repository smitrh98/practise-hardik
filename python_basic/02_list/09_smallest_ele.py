# Python program to find smallest number in a list
li=[23,45,67,89,12,34,56,78]
min=li[0]
for i in li:
    if i<min:
        min=i
print(f'Min : {min}')