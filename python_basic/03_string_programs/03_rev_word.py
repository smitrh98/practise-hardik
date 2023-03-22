# Reverse words in a given String in Python
def rev_words(s):
    s1=s.split()
    sf=''
    for i in s1:
        sf+=i[::-1]+" "
    print(sf)
s="India is 7th largest country in the world."
print(s)
rev_words(s)