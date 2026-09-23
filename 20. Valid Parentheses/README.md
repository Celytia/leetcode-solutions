# 20. Valid Parentheses

### Difficulty: Easy

## Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:


	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.


 
Example 1:


Input: s = "()"

Output: true


Example 2:


Input: s = "()[]{}"

Output: true


Example 3:


Input: s = "(]"

Output: false


Example 4:


Input: s = "([])"

Output: true


Example 5:


Input: s = "([)]"

Output: false


 
Constraints:


	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19456000
- **Language**: python3

## Code
```python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif not stack: 
                return False
            else:
                top=stack.pop()
                if not(top=="(" and i==")" or top=="[" and i=="]" or top=="{" and i=="}" ):
                    return False
        return len(stack)==0
```
