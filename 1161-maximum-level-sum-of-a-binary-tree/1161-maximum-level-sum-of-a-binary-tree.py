# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque

        queue = deque([root]) # Using dequeue because its pop() - O(1)

        max_sum = root.val
        smallest_lvl = 1 # this is the result

        level = 1 # this is counter to track the level we are on

        while queue:
            queue_len = len(queue) # indicates num of nodes in the level
            new_sum = 0
            for _ in range(queue_len):
                node = queue.popleft()
                new_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if new_sum > max_sum:
                smallest_lvl = level
                max_sum = new_sum
            level += 1
                
        return smallest_lvl
        