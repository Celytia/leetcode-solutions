class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=dec=True
        for i in range(1, len(nums)):
            if nums[i - 1] - nums[i]<0:
                dec=False
            elif nums[i - 1] - nums[i]>0:
                inc=False
        if dec==inc==False:
            return False
        else:
            return True