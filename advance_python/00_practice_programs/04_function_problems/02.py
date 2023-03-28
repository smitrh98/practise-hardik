# 2. Write a program to create function calculation() such that it can accept two 
# variables and calculate addition and subtraction. Also, it must return both 
# addition and subtraction in a single return call.
# def decoretor(func):
#     def wrapper(*args):
#         print(f'addition & subtraction of two values:{args}')
#         print(func(*args))
#         print('All done.')
#     return wrapper
# @decoretor

def calculation(a,b):
    add=a+b
    sub=a-b
    return add,sub
print(calculation(102,34))