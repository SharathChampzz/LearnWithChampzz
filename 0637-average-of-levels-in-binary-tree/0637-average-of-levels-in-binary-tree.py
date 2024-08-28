# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return root

        queue = deque([root])

        level_avgs = []

        while queue:
            count = len(queue)
            total_sum = 0

            for _ in range(count):
                node = queue.popleft()
                total_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_avgs.append(round(total_sum / count, 5))

        return level_avgs
