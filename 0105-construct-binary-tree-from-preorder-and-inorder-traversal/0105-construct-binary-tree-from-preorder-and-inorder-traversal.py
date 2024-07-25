# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Notes:
            Preorder: Root Left Right
            Inorder:  Left Root Right

            To start building a tree, you need root node.
            From the available data, we can get that from preorder

            Once we have the root node, we need to decide, what goes to the left and right
            We cant use preorder list for this, because we dont know where to split.
            So find the root in Inorder list, that gives, whatever in the left goes for left tree. right side goes for right tree

            Whatever the mid index in inorder, the same index will be used to split the preorder to decide next root in the left tree and right tree

        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid_index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:mid_index+1], inorder[:mid_index])
        root.right = self.buildTree(preorder[mid_index+1:], inorder[mid_index+1:])

        return root
        