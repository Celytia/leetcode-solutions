class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        res=sum(nums)//len(nums)+1
        if res<=0:
            res=1
        while res in nums:
            res+=1
        return res