#       HINT TAKEN
def flatten_deep(lst):
    l=[]
    for i in lst:
        if type(i)==list:
            l.extend(flatten_deep(i))
        else:
            l.append(i)
    return l

print(flatten_deep([1,[2,[3,4],[]],5]))