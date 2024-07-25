# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True # both have reached end

            if p is None or q is None:
                return False # only one node has reached its end 

            if p.val != q.val:
                return False # value not matching

            left_same = self.isSameTree(p.left, q.left)
            right_same = self.isSameTree(p.right, q.right)

            return left_same and right_same
        