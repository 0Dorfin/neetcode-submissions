class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        visited = set()
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        counter = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)


        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)
        
        return counter