# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        First we will get all the combinations of paths and then take sum of it
        
        We will write a recursive function that helps in building paths and finally return the list of paths
        
        As we are expecting the list as output, we need to ensure, we return list at leaf node as well as the function return at the end.
        Destructure as required
        """
        def build_paths(node, current_path: str):
            if not node:
                return []

            # check if it leaf node
            if node.left is None and node.right is None:
                return [int(current_path + str(node.val))]
            
            left_paths = build_paths(node.left, current_path + str(node.val))
            right_paths = build_paths(node.right, current_path + str(node.val))

            return [*left_paths, *right_paths]
            

        paths = build_paths(root, '')

        return sum(paths)