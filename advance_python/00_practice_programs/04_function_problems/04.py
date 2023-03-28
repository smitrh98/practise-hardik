# 4. Write a function to accept n number of arbitrary arguments of integers are 
# return the sum of the arguments passed
# print(sum([1,2,3,4,5,6,7,8,9,10],start=0))
def sum(*n):
    sum=0
    for i in n:
        sum+=i
    return sum

print(sum(1,2,3,4,5,6,7,8,9,10))
