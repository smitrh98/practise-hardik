# Python program to check if a string is palindrome or not
#1
def palindrome(s):
    s1=s.lower()
    rev=s1[::-1]
    if s1==rev:
        print(f"{s} is palindrome string.")
    else:
        print("Not a palindrome.")
s1="Sahas"
palindrome(s1)
#2
def pldm(s):
    rev=''
    for i in range(len(s)):
        rev+=s[len(s)-1-i]
    if rev==s:
        print("Yes")
    else:
        print("No")
s2="malayalam"
pldm(s2)
