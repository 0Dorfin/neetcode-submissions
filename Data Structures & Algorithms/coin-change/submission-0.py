class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def explore(money_left):
            if money_left == 0:
                return 0
            if money_left < 0:
                return float('inf')
            if money_left in memo:
                return memo[money_left]

            min_coins = float('inf')
            for coin in coins:
                res = 1 + explore(money_left - coin)
                min_coins = min(min_coins, res)

            memo[money_left] = min_coins
            return min_coins
        
        res = explore(amount)
        if res == float('inf'):
            return -1
        else:
            return res