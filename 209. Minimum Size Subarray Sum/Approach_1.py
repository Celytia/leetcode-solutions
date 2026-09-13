class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=j=0
        sum=0
        minlen=float("inf")
        while j<len(nums):
            sum+=nums[j]
            while sum>=target and i<=j:
                minlen=min(minlen,j-i+1)
                sum-=nums[i]
                i+=1
            j+=1
        return minlen if minlen!=float("inf") else 0