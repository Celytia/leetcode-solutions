# 541. Reverse String II

### Difficulty: Easy

## Description
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 
Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

 
Constraints:


	1 <= s.length <= 104
	s consists of only lowercase English letters.
	1 <= k <= 104

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19348000
- **Language**: python3

## Code
```python3
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        pre=0
        while pre+2*k<=len(s):
            s=s[:pre]+s[pre:pre+k][::-1]+s[pre+k:]
            pre+=2*k
        if len(s)-pre<k:
            s=s[:pre]+s[pre:][::-1]
        else:
            s=s[:pre]+s[pre:pre+k][::-1]+s[pre+k:]
        return s
```
