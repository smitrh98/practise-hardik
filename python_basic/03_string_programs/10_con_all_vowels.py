# Python program to accept the strings which contains all vowels
s='ABeeIghiObhkUul'
vowels=set("aeiou")
s1=s.lower()
s=set()
for char in s1:
    if char in vowels:
        s.add(char)
if len(s)==len(vowels):
    print("It's contains all vowels.")
else:
    print("Sorry, Not accepted.")
    