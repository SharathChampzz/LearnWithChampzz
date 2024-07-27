# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def check_sum(node, current_sum):
            if not node:
                return False

            # check if it is leaf node
            if node.left is None and node.right is None:
                return (current_sum + node.val) == targetSum

            left_tree = check_sum(node.left, current_sum + node.val)
            right_tree = check_sum(node.right, current_sum + node.val)

            return left_tree or right_tree

        return check_sum(root, 0)
