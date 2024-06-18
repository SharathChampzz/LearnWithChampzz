# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def bfs():
            if not root: return 0
            from collections import deque

            queue = deque([root])
            depth = 0

            while queue:
                n = len(queue)

                for _ in range(n):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                depth += 1

            return depth

        def dfs():

            def max_depth(node):
                if not node:
                    return 0

                left_depth = max_depth(node.left)
                right_depth = max_depth(node.right)

                return max(left_depth, right_depth) + 1

            return max_depth(root)

        return dfs()
        # return bfs()
        