# 168. Excel Sheet Column Title

### Difficulty: Easy

## Description
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:


A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


 
Example 1:


Input: columnNumber = 1
Output: "A"


Example 2:


Input: columnNumber = 28
Output: "AB"


Example 3:


Input: columnNumber = 701
Output: "ZY"


 
Constraints:


	1 <= columnNumber <= 231 - 1

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19252000
- **Language**: python3

## Code
```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        while columnNumber!=0:
            if columnNumber%26==0:
                s="Z"+s
                columnNumber=columnNumber//26-1
            else:
                s=chr(columnNumber%26+ord("A")-1)+s
                columnNumber=columnNumber//26
        return s
```
