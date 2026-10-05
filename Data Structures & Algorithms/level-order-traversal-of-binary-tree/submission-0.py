# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []

            queue = collections.deque()
            queue.append(root)
            results = []

            while queue:
                level = []
                for i in range(len(queue)):
                    actual_node = queue.popleft()
                    level.append(actual_node.val)
                    if actual_node.left:
                        queue.append(actual_node.left)
                    if actual_node.right:
                        queue.append(actual_node.right)
                results.append(level)
            return results