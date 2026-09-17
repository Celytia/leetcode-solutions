class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        dp=[1]*len(nums)
        maxlen=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                dp[i]=dp[i-1]+1
                maxlen=max(maxlen,dp[i])
        return maxlen
        