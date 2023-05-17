def odd_even_sort(l):
    l.sort()
    odd=[x for x in l if x%2==1]
    even=[x for x in l if x%2==0]
    return odd, even

def quicksort(l):
    if len(l)==0: 
        return []
    else:
        l1=quicksort([x for x in l if x<l[0]])
        l2=[x for x in l if x==l[0]]
        l3=quicksort([x for x in l if x>l[0]])
        return [*l1,*l2,*l3]
l=[2,67,34,32,67,3,11]
print(l)

print(quicksort(l))
odd, even= odd_even_sort(l)
print('odd list: ',odd)
print('even list: ',even)
