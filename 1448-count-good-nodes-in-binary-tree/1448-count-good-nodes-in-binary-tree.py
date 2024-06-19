# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []

        def pre_order(current_node, path):
            if not current_node:
                return
            
            # not path is used to handle empty path at main too node
            # else max([]) would cause exception
            if (not path) or max(path) <= current_node.val:
                good_nodes.append(current_node.val)

            pre_order(current_node.left, path + [current_node.val])
            pre_order(current_node.right, path + [current_node.val])
            

        pre_order(root, [])

        print(f'Good Nodes: {good_nodes}')
        return len(good_nodes)