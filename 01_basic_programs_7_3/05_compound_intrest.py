def c_intrest(p,r,n):
    ci=((1+r/100)**n)*p-p
    return ci
print(c_intrest(10000,12,3))