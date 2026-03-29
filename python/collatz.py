def collatz(n):
    if n!=1:
        print(n, end=",")
    else:
        print(n)
    while n!=1:
        if n%2==0:
            n=n/2
        elif n%2!=0 and n!=1:
            n=3*n+1
        if n!=1:
            print(int(n), end=",")
        else:
            print(int(n))
    return None
collatz(6)
collatz(1)
collatz(3)