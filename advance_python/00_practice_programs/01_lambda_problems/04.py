#Write a Python program to find if a given string starts with a 'Python' using Lambda 
string="Python programming is not good for any bigginer for problemsolving."
if string.startswith('Python'):
    print(True)
else:
    print(False)


start_with=lambda x: True if x.startswith("Python") else False
print(start_with(string))