def transpose(m):
    r=len(m)
    c=len(m[0])
    l=[]
    for i in range(c):
        row=[]
        for j in range(r):
            row.append(m[j][i])
        l.append(row)
    return l

print(transpose([[1,2,3],[4,5,6]]))