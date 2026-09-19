# 383. Ransom Note

### Difficulty: Easy

## Description
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

 
Constraints:


	1 <= ransomNote.length, magazine.length <= 105
	ransomNote and magazine consist of lowercase English letters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 7
- **Memory**: 19680000
- **Language**: python3

## Code
```python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                for j in range(len(magazine)):
                    if i==magazine[j]:
                        if j==0:
                            magazine=magazine[1:]
                        else:
                            magazine=magazine[:j]+magazine[j+1:]
                        break
        return True 
```
