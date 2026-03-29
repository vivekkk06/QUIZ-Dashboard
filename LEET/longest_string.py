def lengthOfLongestSubstring(s: str) -> int:
    l=[]
    a=[]
    for i in s:
        if i not in l:
            l.append(i)
            if s.index(i)==(len(s)-1):
                a.append(len(l))
        else:
            a.append(len(l))
            l.clear()
            l.append(i)
    return max(a)

print(lengthOfLongestSubstring("abcdabcdabcde"))
print(lengthOfLongestSubstring("sdf seccg"))