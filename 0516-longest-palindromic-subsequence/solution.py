class Solution:
    def recursion(self,idx1,idx2,s,dp):
        if idx1 >= idx2:
            if idx1 == idx2:
                return 1
            return 0
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        if s[idx1] == s[idx2]:
            dp[idx1][idx2] =  2 + self.recursion(idx1+1,idx2-1,s,dp)

        else:
            dp[idx1][idx2] = max(self.recursion(idx1+1,idx2,s,dp),self.recursion(idx1,idx2-1,s,dp))
        return dp[idx1][idx2]
        
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        dp=[[-1 for i in range(n+1)]for _ in range(n+1)]
        return self.recursion(0,n-1,s,dp)

        