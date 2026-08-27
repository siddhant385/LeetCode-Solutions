class Solution:
    def memoization(self,idx1,idx2,s,dp):
        if idx1>idx2:
            return 0
        if dp[idx1][idx2] != -1: return dp[idx1][idx2]
        if s[idx1] == s[idx2]:
            dp[idx1][idx2] = self.memoization(idx1+1,idx2-1,s,dp)
            return dp[idx1][idx2]
        
        # if both are different
        dp[idx1][idx2] = min(1 + self.memoization(idx1+1,idx2,s,dp),1 + self.memoization(idx1,idx2-1,s,dp))
        return dp[idx1][idx2]



    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(1+dp[i+1][j],1+dp[i][j-1])
        return dp[0][n-1]
        