
def gcd(a,b):
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            g=i
    return g

print(gcd(12,8))
print(gcd(20,15))
print(gcd(100,80))
print(gcd(7,3))
print(gcd(9,6))
print(gcd(81,27))
print(gcd(17,13))
print(gcd(56,42))
print(gcd(121,11))