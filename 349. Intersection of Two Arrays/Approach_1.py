class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=[0]*1001
        n2=[0]*1001
        result=[]
        for i in range(len(nums1)):
            n1[nums1[i]]+=1
        for i in range(len(nums2)):
            n2[nums2[i]]+=1
        for i in range(1001):
            if n1[i]*n2[i]>0:
                result.append(i)
        return result