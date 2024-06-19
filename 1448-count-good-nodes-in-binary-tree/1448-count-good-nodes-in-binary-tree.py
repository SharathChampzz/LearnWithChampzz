# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []

        def pre_order(current_node, max_element_so_far):
            if not current_node:
                return
            
            # We will check if there was any big element found in the path
            if max_element_so_far <= current_node.val:
                good_nodes.append(current_node.val)
                max_element_so_far = current_node.val # current node is bigger/equal than all previous

            pre_order(current_node.left, max_element_so_far)
            pre_order(current_node.right, max_element_so_far)
            

        pre_order(root, root.val)

        print(f'Good Nodes: {good_nodes}')
        return len(good_nodes)