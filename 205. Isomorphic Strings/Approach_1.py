class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        idxt=[0]*200
        idxs=[0]*200
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if idxt[ord(t[i])]!=idxs[ord(s[i])]:
                return False
            idxt[ord(t[i])]=i+1
            idxs[ord(s[i])]=i+1
        return True