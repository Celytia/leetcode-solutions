# 3541. Find Most Frequent Vowel and Consonant

### Difficulty: Easy

## Description
You are given a string s consisting of lowercase English letters ('a' to 'z'). 

Your task is to:


	Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
	Find the consonant (all other letters excluding vowels) with the maximum frequency.


Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
The frequency of a letter x is the number of times it occurs in the string.
 
Example 1:


Input: s = "successes"

Output: 6

Explanation:


	The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
	The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
	The output is 2 + 4 = 6.



Example 2:


Input: s = "aeiaeia"

Output: 3

Explanation:


	The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
	There are no consonants in s. Hence, maximum consonant frequency = 0.
	The output is 3 + 0 = 3.



 
Constraints:


	1 <= s.length <= 100
	s consists of lowercase English letters only.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19352000
- **Language**: python3

## Code
```python3
class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic={"a":0,"e":0,"i":0,"o":0,"u":0}
        lst=[0]*26
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                lst[ord(i)-ord("a")]+=1
        return dic[max(dic,key=dic.get)]+max(lst)
```
