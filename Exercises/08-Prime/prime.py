plist=[2] #2 is the smallest prime
hl=list(range(3,251)) 

while plist[-1]**2<hl[-1]: # you only have to consider devisors, which are smaller than the squareroot of the maximal number
    hl=[x for x in hl if x % plist[-1]!=0] # a prime is a number, which is only devisible by 1 and itself
    plist.append(hl[0])
    hl=hl[1:]

plist=plist+hl
primes=', '.join([str(x) for x in plist])
print(primes)
with open(r'Exercises\08-Prime\results.txt','w')  as file:
    for x in plist:
        file.write(str(x)+'\n')
