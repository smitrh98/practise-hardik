def sym_plm(s):
    s1=s[::-1]
    s2=s[int(len(s)/2):]
    if s==s1:
        print("It is Palindrome string.")
    elif s[:int(len(s)/2)]==s2:
        print("It is Symmetric string.")
    else:
        print("Not Palindrome and not Symmetric.")
a='stringstring'
sym_plm(a) 
b="malayalam"
sym_plm(b)
c='abcdecba'
sym_plm(c)