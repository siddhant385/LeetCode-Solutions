class Solution:
    def byRecursion(self,r,c,dp):
        if r < 0 or c < 0:
            return 0
        if (r,c) == (0,0):
            return 1
        if dp[r][c] != -1:
            return dp[r][c]
        
        dp[r][c] = self.byRecursion(r,c-1,dp) + self.byRecursion(r-1,c,dp)
        return dp[r][c]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for _ in range(m)]
        return self.byRecursion(m-1,n-1,dp)
        
        