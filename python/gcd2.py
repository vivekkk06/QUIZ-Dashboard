def gcd(a,b):

    x=min([abs(a),abs(b)])

    for i in range(1,x+1):
        if a%i==0 and b%i==0:
            e=i
    return e
print(gcd(-5,-10))