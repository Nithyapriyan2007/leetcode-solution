class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def helper(step: int) -> int:

            if step < 0:
                return 0

            if step == 0:
                return 1

            if dp[step] != -1:
                return dp[step]

            dp[step] = helper(step - 1) + helper(step - 2)

            return dp[step]

        return helper(n)