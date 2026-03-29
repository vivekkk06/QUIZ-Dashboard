def print_sum(num1):
    num=int(num1)
    s=0
    while num>0:
        s=s+(num%10)
        num=num//10
    return s

print(print_sum("8097"))
print(print_sum("2345"))
print(print_sum("5678097"))
print(print_sum("50"))
print(print_sum("0"))