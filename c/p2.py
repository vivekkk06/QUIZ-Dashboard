x=str(input())
y=str(input())
a=x.split()
a1=[]
b=y.split()
b1=[]
c=[]
for i in range(len(a)):
    if i%2==1:
        a1.append(a[i])
a1=sorted(a1)

for i in range(len(b)):
    if i%2==1:
        b1.append(b[i])
b1=sorted(b1)

if len(a1)<=len(b1):
    for i in a1:
        if i in b1:
            c.append(str(int(a[a.index(i)-1]) + int(b[b.index(i)-1])))
            c.append(i)
        else:
            c.append(a[a.index(i)-1])
            c.append(i)
else:
    for i in b1:
        if i in a1:
            c.append(str(int(b[b.index(i)-1]) + int(a[a.index(i)-1])))
            c.append(i)
        else:
            c.append(b[b.index(i)-1])
            c.append(i)
c1=[]
for i in range(len(c)):
    if i%2==1:
        c1.append(c[i])
for i in a1:
    if i not in c1:
        c.append(a[a.index(i)-1])
        c.append(i)
for i in b1:
    if i not in c1:
        c.append(b[b.index(i)-1])
        c.append(i)

c1=[]
for i in range(len(c)):
    if i%2==1:
        c1.append(c[i])
c1=sorted(c1)
d=[]
for i in range(1,len(c1)):
    d.append(c[c.index(c1[i])-1])
    d.append(c1[i])

s=d[0]
for i in range(1,len(d)):
    s=s+" "+d[i]
print(s)