class Solution:
    def recursion(self,idx1,idx2,s,dp):
        if idx1>idx2:
            return 0
        if dp[idx1][idx2] != -1: return dp[idx1][idx2]
        if s[idx1] == s[idx2]:
            dp[idx1][idx2] = self.recursion(idx1+1,idx2-1,s,dp)
            return dp[idx1][idx2]
        
        # if both are different
        dp[idx1][idx2] = min(1 + self.recursion(idx1+1,idx2,s,dp),1 + self.recursion(idx1,idx2-1,s,dp))
        return dp[idx1][idx2]



    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)]for _ in range(n)]
        return self.recursion(0,n-1,s,dp)
        