# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        queue = deque([root])
        level = 0
        result = list()

        while queue:
            n = len(queue)
            temp_result = list()

            while n:
                node = queue.popleft()
                temp_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                n -= 1
            
            # if it is even
            if level % 2 == 0:
                result.append(temp_result)
            else:
                result.append(temp_result[::-1])
            level += 1

        return result