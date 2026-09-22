# 234. Palindrome Linked List

### Difficulty: Easy

## Description
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 
Example 1:


Input: head = [1,2,2,1]
Output: true


Example 2:


Input: head = [1,2]
Output: false


 
Constraints:


	The number of nodes in the list is in the range [1, 105].
	0 <= Node.val <= 9


 
Follow up: Could you do it in O(n) time and O(1) space?

## Submission Details
- **Status**: Accepted
- **Runtime**: 75
- **Memory**: 53964000
- **Language**: python3

## Code
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        s=""
        cur=head
        while cur:
            s+=str(cur.val)
            cur=cur.next
        if s==s[::-1]:
            return True
        return False
```
