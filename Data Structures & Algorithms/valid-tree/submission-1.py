class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        visited = set()
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == prev:
                    continue
            
                if not dfs(neighbour, node):
                    return False

            return True

        return dfs(0,-1) and n == len(visited)