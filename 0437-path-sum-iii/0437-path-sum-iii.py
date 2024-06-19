# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def post_order(current_node, path):
            nonlocal result

            if not current_node:
                return

            new_path = [current_node.val] + path # add new value to the begining

            post_order(current_node.left, new_path)
            post_order(current_node.right, new_path)

            current_sum = 0
            # we will have iterate through full list because there can be negative numbers subtracting it might get us the target
            for i in new_path:
                current_sum += i
                if current_sum == targetSum:
                    print(result)
                    result += 1
                    # break # we cant use break, we want to find if the next elements can also result into the targetSum example: -1,+1

        post_order(root, [])

        return result

