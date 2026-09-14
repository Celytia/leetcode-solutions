class Solution:
    def isHappy(self, n: int) -> bool:
        count=[]
        while n not in count:
            count.append(n)
            sum=0
            for i in str(n):
                sum+=int(i)**2
            if sum==1:
                return True
            n=sum
        return False