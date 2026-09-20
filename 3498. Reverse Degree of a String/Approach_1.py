class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(1,len(s)+1):
            alp=26-(ord(s[i-1])-ord("a"))
            sum+=alp*i
        return sum