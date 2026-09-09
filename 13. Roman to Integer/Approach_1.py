class Solution:
    def romanToInt(self, s: str) -> int:
        r={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        m={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        sum=0
        i=len(s)-1
        while i>0:
            if s[i-1:i+1] in m:
                sum+=m[s[i-1:i+1]]
                s=s[:i-1]
                i-=2
            else:
                sum+=r[s[i]]
                s=s[:i]
                i-=1
        if i==0:
            sum+=r[s[0]]
        return sum


