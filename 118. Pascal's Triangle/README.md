# 118. Pascal's Triangle

### Difficulty: Easy

## Description
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

 
Constraints:


	1 <= numRows <= 30

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19352000
- **Language**: python3

## Code
```python3
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows==0:
            return None
        if numRows==1:
            return [[1]]
        prev=self.generate(numRows-1)
        new=[1]*numRows
        for i in range(1,numRows-1):
            new[i]=prev[-1][i-1]+prev[-1][i]
        prev.append(new)
        return prev
```
