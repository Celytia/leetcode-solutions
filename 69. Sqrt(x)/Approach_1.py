class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        while ans*ans<=x:
            ans+=1
            product=ans*ans
        if x-product<ans*ans-x:
            return ans-1
        else:
            return ans