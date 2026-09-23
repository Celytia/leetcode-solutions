class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        flag=[1]*len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]<target:
                flag[i]=-1
            elif i==0 or flag[i-1]==-1:
                return i
        if flag[-1]==-1:
            return len(nums)