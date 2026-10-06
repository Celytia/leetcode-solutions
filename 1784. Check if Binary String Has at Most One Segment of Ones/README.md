# 1784. Check if Binary String Has at Most One Segment of Ones

### Difficulty: Easy

## Description
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 
Example 1:


Input: s = "1001"
Output: false
Explanation: The string has two segments of size 1.


Example 2:


Input: s = "110"
Output: true

 
Constraints:


	1 <= s.length <= 100
	s[i]​​​​ is either '0' or '1'.
	s[0] is '1'.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19208000
- **Language**: python3

## Code
```python3
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt=0
        flag=True
        s=s+"0"
        for i in s:
            if i=="1":
                flag=False
            if not flag and i=="0":
                cnt+=1
                flag=True
        if cnt<2:
            return True
        else:
            return False
```
