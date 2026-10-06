class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def explore(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            res = explore(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += explore(i + 2)
            memo[i] = res
            return res

        return explore(0)