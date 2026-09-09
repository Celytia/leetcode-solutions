class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        if n==2 and s[0]==s[1]:
            return True
        for i in range(1,n-1):
            if n%i!=0:
                continue
            else:
                if s==s[:i]*int(n/i):
                    return True
        return False