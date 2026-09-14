# 349. Intersection of Two Arrays

### Difficulty: Easy

## Description
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 
Example 1:


Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]


Example 2:


Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


 
Constraints:


	1 <= nums1.length, nums2.length <= 1000
	0 <= nums1[i], nums2[i] <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 2
- **Memory**: 19388000
- **Language**: python3

## Code
```python3
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
```
