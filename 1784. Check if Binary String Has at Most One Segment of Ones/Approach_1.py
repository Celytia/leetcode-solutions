class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt=0
        flag=True
        s=s+"0"
        for i in s:
            if i=="1":
                flag=False
            if not flag and i=="0":
                cnt+=1
                flag=True
        if cnt<2:
            return True
        else:
            return False