class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        pre=0
        while pre+2*k<=len(s):
            s=s[:pre]+s[pre:pre+k][::-1]+s[pre+k:]
            pre+=2*k
        if len(s)-pre<k:
            s=s[:pre]+s[pre:][::-1]
        else:
            s=s[:pre]+s[pre:pre+k][::-1]+s[pre+k:]
        return s