class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=[]
        for i in range(m):
            arr.append(nums1[i])
        for i in nums2:
            arr.append(i)
        arr.sort()
        for i in range(m+n):
            nums1[i]=arr[i]