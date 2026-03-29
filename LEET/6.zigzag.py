def convert(s: str, n: int) -> str:
    s=""
    for i in s:
        if s.index(i) % n+1:
            s=s+i
    for i in s:
        if 