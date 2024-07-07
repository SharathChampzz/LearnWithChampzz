# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_count = 0

        def zig_zag(node, is_left, is_right, count):
            nonlocal max_count
            if not node:
                return

            if is_left:
                zig_zag(node.right, 0, 1, count+1)
                zig_zag(node.left, 1, 0, 1)
            elif is_right:
                zig_zag(node.left, 1, 0, count+1)
                zig_zag(node.right, 0, 1, 1)
            else: # root node
                zig_zag(node.left, 1, 0, 1)
                zig_zag(node.right, 0, 1, 1)

            max_count = max(count, max_count)

        zig_zag(root, 0, 0, 0)

        return max_count
        