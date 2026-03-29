l=[3,5,7]
k=1
def no_operations(l,k):
    s=0
    for i in l:
        while i>0:
            i=i-k
            s+=1
    return s
def min_k(l,k):
    a = k**2 - no_operations(l,k)
    if a >= 0:
        return k
    else:
        return min_k(l, k + 1)

print(min_k(l,k))