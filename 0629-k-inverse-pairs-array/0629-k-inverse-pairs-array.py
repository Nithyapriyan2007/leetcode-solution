class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            ndp = [0] * (k + 1)
            for j in range(k + 1):
                ndp[j] = (dp[j] + (ndp[j-1] if j else 0)) % MOD
                if j >= i:
                    ndp[j] = (ndp[j] - dp[j-i]) % MOD
            dp = ndp
        return dp[k]