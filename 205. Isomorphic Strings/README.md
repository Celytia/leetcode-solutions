# 205. Isomorphic Strings

### Difficulty: Easy

## Description
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 
Example 1:


Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:


	Mapping 'e' to 'a'.
	Mapping 'g' to 'd'.



Example 2:


Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.


Example 3:


Input: s = "paper", t = "title"

Output: true


 
Constraints:


	1 <= s.length <= 5 * 104
	t.length == s.length
	s and t consist of any valid ascii character.

## Submission Details
- **Status**: Accepted
- **Runtime**: 6
- **Memory**: 19196000
- **Language**: python3

## Code
```python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        idxt=[0]*200
        idxs=[0]*200
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if idxt[ord(t[i])]!=idxs[ord(s[i])]:
                return False
            idxt[ord(t[i])]=i+1
            idxs[ord(s[i])]=i+1
        return True
```
