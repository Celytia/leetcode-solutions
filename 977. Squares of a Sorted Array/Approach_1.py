class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[0]*n
        l,r,i=0,n-1,n-1
        while l<=r and i>=0:
            if nums[l]**2<nums[r]**2:
                a[i]=nums[r]**2
                r-=1
            elif nums[l]**2>=nums[r]**2:
                a[i]=nums[l]**2
                l+=1
            i-=1
        return a