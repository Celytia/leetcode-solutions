# 35. Search Insert Position

### Difficulty: Easy

## Description
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:


Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:


Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:


Input: nums = [1,3,5,6], target = 7
Output: 4


 
Constraints:


	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums contains distinct values sorted in ascending order.
	-104 <= target <= 104

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19996000
- **Language**: python3

## Code
```python3
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
```
