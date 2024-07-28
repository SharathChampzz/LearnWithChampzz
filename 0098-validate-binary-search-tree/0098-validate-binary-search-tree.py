# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Note: In a valid BST, inorder traversal of tree should give sorted output in increasing order

        So we will keep track prev element and always ensure new element is greater than previous
        """
        prev = -float('inf')

        def inorder(node):
            nonlocal prev

            if not node:
                return True # end or no node exists

            left_status = inorder(node.left)

            if node.val <= prev:
                return False

            prev =  node.val # update the previous value to the current

            right_status = inorder(node.right)

            return left_status and right_status

        return inorder(root)
        