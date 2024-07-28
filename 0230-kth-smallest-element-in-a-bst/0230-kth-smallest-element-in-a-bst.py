# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_k = 0
        result_found = None

        def inorder(node):
            nonlocal k, current_k, result_found

            if not node:
                return

            if result_found:
                return  # result already found, go back

            inorder(node.left)
            current_k += 1

            if current_k == k:
                result_found = node.val
                return

            inorder(node.right)

        inorder(root)
        return result_found
