class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return min(1, n)
            
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]