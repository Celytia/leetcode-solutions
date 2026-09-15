class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt=0
        i,j=len(g)-1,len(s)-1
        while j>=0 and i>=0:
            if s[j]>=g[i]:
                cnt+=1
                j-=1
            i-=1
        return cnt