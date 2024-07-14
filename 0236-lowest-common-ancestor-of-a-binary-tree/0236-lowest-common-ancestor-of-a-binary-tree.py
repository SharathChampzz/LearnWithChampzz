# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base cases
        if not root:
            return None
        if root is p or root is q:
            return root

        # Recursively search for p and q in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees found an LCA, then the current node is the LCA.
        if left_lca and right_lca:
            return root

        # Otherwise, return the LCA found in either left or right subtree.
        return left_lca if left_lca else right_lca

            


        


        