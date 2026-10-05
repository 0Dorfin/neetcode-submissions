# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, min_node, max_node):
            if not node:
                return True

            if node.val <= min_node or node.val >= max_node:
                return False

            left = validate(node.left, min_node, node.val)
            right = validate(node.right, node.val, max_node)

            return left and right

        return validate(root, float('-inf'), float('inf'))

        
