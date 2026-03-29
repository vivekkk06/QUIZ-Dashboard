'''
def concat_even(lst):
    n=len(lst)
    a=""
    if(n!=0):
        for i in lst:
            if(lst.index(i)%2==0):
                if((lst.index==n-1) or (lst.index==n-2)):
                    a=a+i
                else:
                    a = a + (i+"#")
        return a
    else:
        return ""

print(concat_even(["a","g","6","7"]))
'''
def concat_even(lst):
    l=[]
    for i in lst:
        if lst.index(i)%2==0:
            l.append(i)
    return "#".join(l)
print(concat_even(["a","g","6","7","k","0"]))
print(concat_even(["p"]))
print(concat_even([]))