def print_sum(num):
    l=len(num)
    m=int(num)
    s=0
    for i in range(1,l+1):
        if(m>=10):
            s=s+(m%(10))
            m=m // (10)
        else:
            s=s+m
    return s

print(print_sum("2345"))
print(print_sum("5678097"))
print(print_sum("50"))
print(print_sum("0"))