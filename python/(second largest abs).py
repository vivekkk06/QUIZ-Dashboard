def sec_larg_abs(lst:list):

    m=(lst[0])
    for i in lst:
        if(abs(i)>abs(m)):
            m=i
    lst.remove(m)
    m=lst[0]
    for i in lst:
        if(abs(i)>abs(m)):
            m=i
    return m

print(sec_larg_abs([8,9,4,45]))
print(sec_larg_abs([-10,8,-9]))
print(sec_larg_abs([-8,8]))
print(sec_larg_abs([-8,98]))