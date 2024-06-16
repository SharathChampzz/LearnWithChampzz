# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # first find that element
        # check if it is leaf node (return None), or has only one children (return Node which is not None)
        # if it has both the childdren, we will to go to right side of the tree and get the left most value
        # copy this value and update to the node to be deleted (Now the node is kinda successfully deleted)
        # Remove that left most node as we copied the value, we dont need it anymore.
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key is found
            # if it is leaf node
            if root.left is None and root.right is None:
                return None

            # if it has only one child node
            if root.left and root.right is None: return root.left
            if root.right and root.left is None: return root.right

            # if it has two child-nodes
            temp_node = root.right
            while temp_node.left:
                temp_node = temp_node.left

            root.val = temp_node.val # pick the last left value and update the node which was supposed to be deleted

            # delete that last left value node now
            root.right = self.deleteNode(root.right, temp_node.val)

        return root
        