class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=f=0
        n=len(nums)
        while f<n:
            if nums[f]!=val:
                nums[s]=nums[f]
                s+=1
            f+=1
        return s
