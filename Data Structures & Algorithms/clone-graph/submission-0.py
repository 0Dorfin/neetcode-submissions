"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        dict_graph = {}

        def dfs(node):
            if node in dict_graph:
                return dict_graph[node]
            
            clon = Node(node.val)
            dict_graph[node] = clon

            for neighbour in node.neighbors:
                clon.neighbors.append(dfs(neighbour))
            return clon

        return dfs(node)