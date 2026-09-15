class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)
        i=0
        while k>0 and i<len(nums):
            if nums[i]<0:
                nums[i]=-nums[i]
                k-=1
            i+=1
        if k%2==1:
            nums[-1]=-nums[-1]
        return sum(nums)


