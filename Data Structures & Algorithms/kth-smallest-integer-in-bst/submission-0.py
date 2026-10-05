# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.contador = 0
        self.resultado = None
        
        def inorder(node):
            if not node:
                return None

            if self.resultado is not None:
                return
            
            inorder(node.left)
            self.contador += 1
            if self.contador == k:
                self.resultado = node.val
            inorder(node.right)
            
        inorder(root)
        return self.resultado