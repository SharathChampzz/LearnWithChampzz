# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Level order traversal means BFS, which means queue. 
        
        How it works? Whenever you pop an element, you make sure to insert left and right node.
        How to get elements belonging to level? you will have to check number of elements present in the queue and pop those elements, while making sure you push left and right values into the queue.
        If there were "n" elements, loop should only run for n times
        """
        if not root:
            return

        queue = deque([root])
        result = []

        while queue:
            n = len(queue)
            temp_result = []

            while n:
                node = queue.popleft()
                temp_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                n -= 1

            result.append(temp_result)

        return result