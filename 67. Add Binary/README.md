# 67. Add Binary

### Difficulty: Easy

## Description
Given two binary strings a and b, return their sum as a binary string.

 
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

 
Constraints:


	1 <= a.length, b.length <= 104
	a and b consist only of '0' or '1' characters.
	Each string does not contain leading zeros except for the zero itself.

## Submission Details
- **Status**: Accepted
- **Runtime**: 6
- **Memory**: 19452000
- **Language**: python3

## Code
```python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=""
        m=0
        if len(a)<=len(b):
            for i in range(1,len(a)+1):
                t=int(a[len(a)-i])+int(b[len(b)-i])+m
                s=str(t%2)+s
                m=t//2
            for i in range(len(b)-len(a)-1,-1,-1):
                t=int(b[i])+m
                s=str(t%2)+s
                m=t//2
        else:
            for i in range(1,len(b)+1):
                t=int(b[len(b)-i])+int(a[len(a)-i])+m
                s=str(t%2)+s
                m=t//2
            for i in range(len(a)-len(b)-1,-1,-1):
                t=int(a[i])+m
                s=str(t%2)+s
                m=t//2
        if m==1:
                s="1"+s
        return s
```
