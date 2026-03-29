class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) != len(p):
            return False
        else:
            for i in range(0,len(s)):
                if s[i] == p[i]:
                    pass
                elif p[i]==".":
                    pass
                elif p[i]=="*":
                    if i==0:
                        if s[i]==0:
                            pass
                        else:
                            return False
                    elif p[i-1]==".":
                        pass
                    elif p[i-1]!=s[i]:
                        return False
                elif s[i]!=p[i]:
                    return False
            return True       
                
            