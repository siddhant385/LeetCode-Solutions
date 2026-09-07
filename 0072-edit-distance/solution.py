class Solution:
    def recursion(self,i,j,word1,word2):
        if j < 0:
            return i+1
        if i < 0:
            return j+1
        if word1[i] == word2[j]:
            return self.recursion(i-1,j-1,word1,word2)
        return 1 + min(self.recursion(i-1,j,word1,word2),self.recursion(i-1,j-1,word1,word2),self.recursion(i,j-1,word1,word2))
    def memoization(self,i,j,word1,word2,dp):
        if j < 0:
            return i+1
        if i < 0:
            return j+1
        if dp[i][j] != -1: return dp[i][j]
        if word1[i] == word2[j]:
            dp[i][j] = self.memoization(i-1,j-1,word1,word2,dp)
        else:
            dp[i][j] = 1 + min(self.memoization(i-1,j,word1,word2,dp),self.memoization(i-1,j-1,word1,word2,dp),self.memoization(i,j-1,word1,word2,dp))
        return dp[i][j]
        
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1 for i in range(n)]for _ in range(m)]
        return self.memoization(m-1,n-1,word1,word2,dp)