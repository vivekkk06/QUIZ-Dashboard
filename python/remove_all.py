def remove_all(a,b):
    l=[]
    for i in a:
        if i!=b:
            l.append(i)
    return l

print(remove_all([1,2,3,1,2,5,1],1))