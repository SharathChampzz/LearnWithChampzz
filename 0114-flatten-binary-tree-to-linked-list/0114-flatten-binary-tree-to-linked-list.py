# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        Notes:
            The result should be a pre-order so: Root => Left => Right
            
            It indicates we need to solve the left, right tree and then insert left in between the root and the right node.
            So flatten left and right tree recursively
            
            Either of tree side, once we flatten, we need tail. 
            So that we can can attach left side tress tail to end top of the right side tree and insert left in between root and right
        
        """
        if not root:
            return None

        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail or left_tail or root