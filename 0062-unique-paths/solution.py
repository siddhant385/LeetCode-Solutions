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
        prev = [-1 for _ in range(n)]
        prev[0] = 1

        for r in range(m):
            curr = [1 for _ in range(n)]
            for c in range(n):
                if (r,c) == (0,0):
                    continue
                curr[c] = 0
                if r-1 > -1:
                    curr[c] += prev[c]
                if c-1 > -1:
                    curr[c] += curr[c-1]
            prev = curr
        return prev[c]
        
        