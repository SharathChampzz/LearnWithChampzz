# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp_node = root

        while temp_node:
            if val == temp_node.val:
                return temp_node
            elif val < temp_node.val:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        return None

        