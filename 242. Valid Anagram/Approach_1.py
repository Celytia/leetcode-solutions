class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=False
        if len(s)!=len(t):
            return flag
        letter=[0]*26
        for i in range(len(s)):
            letter[ord(s[i])-ord("a")]+=1
        for i in range(len(t)):
            letter[ord(t[i])-ord("a")]-=1
        if letter==[0]*26:
            flag=True
        return flag