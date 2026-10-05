class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robber(houses):
            n = len(houses)
            dp = [0] * n

            if n == 1:
                return houses[0]

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            
            return dp[-1]

        robber_a = robber(nums[1:])
        robber_b = robber(nums[:-1])

        return max(robber_a, robber_b)