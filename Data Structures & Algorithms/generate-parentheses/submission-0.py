class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        path = []

        abiertos = 0
        cerrados = 0

        def backtrack(abiertos, cerrados, path):
            if abiertos == n and cerrados == n:
                results.append(''.join(path))
                return
            
            if abiertos < n:
                path.append('(')
                backtrack(abiertos + 1, cerrados, path)
                path.pop()

            if cerrados < abiertos:
                path.append(')')
                backtrack(abiertos, cerrados + 1, path)
                path.pop()

        backtrack(abiertos, cerrados, path)
        return results