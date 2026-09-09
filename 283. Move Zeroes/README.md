# 283. Move Zeroes

### Difficulty: Easy

## Description
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

 
Constraints:


	1 <= nums.length <= 104
	-231 <= nums[i] <= 231 - 1


 
Follow up: Could you minimize the total number of operations done?

## Submission Details
- **Status**: Accepted
- **Runtime**: 6
- **Memory**: 20452000
- **Language**: python3

## Code
```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        cnt=0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt+=1
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(len(nums)-cnt,len(nums)):
            nums[i]=0
        return nums
                
```
