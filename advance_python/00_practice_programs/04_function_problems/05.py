# 5. Write a function to accept n number of keyword arguments and print them
def func(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
func(a=1,b=2,c=3,d=4,e=5)

# def func(**kwargs):
#     for kwarg in kwargs.items():
#         print(kwarg)
# func(a=1,b=2,c=3,d=4,e=5)
