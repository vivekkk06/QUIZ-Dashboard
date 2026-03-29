def merge_list(a,b):
    l=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if(a[i]<b[j]):
            l.append(a[i])
            i+=1
        else:
            l.append(b[j])
            j+=1
    while i<len(a):
        l.append(a[i])
        i+=1
    while j<len(b):
        l.append(b[j])
        j+=1
    return l

print(merge_list([1,2,3],[1.5,8,9]))
print(merge_list([1,3,5],[2,4,6]))
