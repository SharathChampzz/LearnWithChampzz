# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def post_order(current_node, path):
            nonlocal result

            if not current_node:
                return

            # Append the current node's value to the existing path
            path.append(current_node.val)

            post_order(current_node.left, path)
            post_order(current_node.right, path)

            current_sum = 0
            # Iterate through the path in reverse to check for targetSum
            for i in range(len(path) - 1, -1, -1):
                current_sum += path[i]
                if current_sum == targetSum:
                    result += 1

            # Remove the current node's value before returning to the caller
            path.pop()

        post_order(root, [])

        return result