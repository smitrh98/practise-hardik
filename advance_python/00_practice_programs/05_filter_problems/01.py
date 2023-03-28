# 1.Filters vowels in a given list.
# sequence  = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
l1=['g', 'e', 'e', 'j', 'k', 's', 'p', 'r', 'A']
result=list(filter(lambda x:x.lower() in ('a','e','i','o','u'),l1))
print(result)