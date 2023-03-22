def armstrong(x):
    i=len(str(x))
    y=x
    s=0
    while(x>0):
        n=x%10
        s=s+n**i
        x=x//10
    if s==y:
        print(f'{y} is an armstrong number.')
    else:
        print(f'{y} is not an armsrong number.')
armstrong(9474)