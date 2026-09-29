# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self,left,right):
            if not left and not right:
                return True
            if not left or not right or left.val!=right.val:
                return False
            return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.mirror(root.left,root.right)
     