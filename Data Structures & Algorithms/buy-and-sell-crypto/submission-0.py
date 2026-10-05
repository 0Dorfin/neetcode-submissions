class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0

        for R in range(1, len(prices)):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
                R += 1
            else:
                L = R
        return max_profit