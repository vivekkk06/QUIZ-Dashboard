def unique_preserve(lst):
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    return l

print(unique_preserve([1,4,1,4,3]))