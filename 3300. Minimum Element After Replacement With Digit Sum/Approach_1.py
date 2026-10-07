class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=36
        for i in nums:
            ans=min(ans,i%10+i//10%10+i//100%10+i//1000%10+i//10000)
        return ans