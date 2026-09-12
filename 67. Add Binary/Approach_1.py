class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=""
        m=0
        if len(a)<=len(b):
            for i in range(1,len(a)+1):
                t=int(a[len(a)-i])+int(b[len(b)-i])+m
                s=str(t%2)+s
                m=t//2
            for i in range(len(b)-len(a)-1,-1,-1):
                t=int(b[i])+m
                s=str(t%2)+s
                m=t//2
        else:
            for i in range(1,len(b)+1):
                t=int(b[len(b)-i])+int(a[len(a)-i])+m
                s=str(t%2)+s
                m=t//2
            for i in range(len(a)-len(b)-1,-1,-1):
                t=int(a[i])+m
                s=str(t%2)+s
                m=t//2
        if m==1:
                s="1"+s
        return s