class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum=0
            for j in range(len(str(nums[i]))):
                sum+=int(str(nums[i])[j])
            if sum==i:
                return i
        return -1