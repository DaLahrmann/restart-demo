def fac1(n):
    if n<0:
        print('factorial not defined')
        return 0
    f=1
    for i in range(n):
        f*=(i+1)
    return f

def fac2(n):
    if n<0:
        print('factorial not defined')
        return 0
    elif n==0: 
        return 1
    else:
        return n*fac2(n-1)

n=500
print(n,fac1(n),fac2(n))