# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using DFS algo
        
        if not root:
            return root

        queue = deque([root])
        result = []

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(node.val)

        return result







    def OldrightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        node = root

        result.append(node.val)

        while node.left or node.right:
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                break
            result.append(node.val)
        
        return result
