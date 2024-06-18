# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_nodes(root):
            if not root:
                return []
                
            if not root.left and not root.right:
                return [root.val]

            left = get_leaf_nodes(root.left)
            right = get_leaf_nodes(root.right)

            return left + right

        leafs_1 = get_leaf_nodes(root1)
        leafs_2 = get_leaf_nodes(root2)

        return leafs_1 == leafs_2

