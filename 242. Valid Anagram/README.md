# 242. Valid Anagram

### Difficulty: Easy

## Description
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
Example 1:


Input: s = "anagram", t = "nagaram"

Output: true


Example 2:


Input: s = "rat", t = "car"

Output: false


 
Constraints:


	1 <= s.length, t.length <= 5 * 104
	s and t consist of lowercase English letters.


 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Submission Details
- **Status**: Accepted
- **Runtime**: 15
- **Memory**: 19400000
- **Language**: python3

## Code
```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=False
        if len(s)!=len(t):
            return flag
        letter=[0]*26
        for i in range(len(s)):
            letter[ord(s[i])-ord("a")]+=1
        for i in range(len(t)):
            letter[ord(t[i])-ord("a")]-=1
        if letter==[0]*26:
            flag=True
        return flag
```
