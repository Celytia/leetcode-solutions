# 459. Repeated Substring Pattern

### Difficulty: Easy

## Description
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 
Example 1:


Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.


Example 2:


Input: s = "aba"
Output: false


Example 3:


Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


 
Constraints:


	1 <= s.length <= 104
	s consists of lowercase English letters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 11
- **Memory**: 19152000
- **Language**: python3

## Code
```python3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        if n==2 and s[0]==s[1]:
            return True
        for i in range(1,n-1):
            if n%i!=0:
                continue
            else:
                if s==s[:i]*int(n/i):
                    return True
        return False
```
