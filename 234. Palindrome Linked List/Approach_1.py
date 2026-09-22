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