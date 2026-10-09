class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ans=[]
        s=f=0
        while f<len(nums)-1:
            if nums[f]+1==nums[f+1]:
                f+=1
            else:
                if s==f:
                    ans.append(str(nums[s]))
                else:
                    ans.append(str(nums[s])+"->"+str(nums[f]))
                s=f=f+1
        if s==f:
            ans.append(str(nums[s]))
        else:
            ans.append(str(nums[s])+"->"+str(nums[f]))
        return ans