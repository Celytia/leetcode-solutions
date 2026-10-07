# 3300. Minimum Element After Replacement With Digit Sum

### Difficulty: Easy

## Description
You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 
Example 1:


Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.


Example 2:


Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.


Example 3:


Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.


 
Constraints:


	1 <= nums.length <= 100
	1 <= nums[i] <= 104

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19308000
- **Language**: python3

## Code
```python3
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=36
        for i in nums:
            ans=min(ans,i%10+i//10%10+i//100%10+i//1000%10+i//10000)
        return ans
```
