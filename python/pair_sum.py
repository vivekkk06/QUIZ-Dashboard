def pair_sum(lst):
    l=[]
    for i in range(0,len(lst)-1):
        a=lst[i]+lst[i+1]
        if a not in l:
            l.append(a)
    return l

print(pair_sum([1,2,3,4]))
print(pair_sum([9]))
print(pair_sum([]))