class Solution:
    def recursion(self,idx1,idx2,word1,word2,dp):
        if idx1 <0 or idx2<0:
            if idx1 < 0:
                return idx2+1
            else:
                return idx1+1
        if dp[idx1][idx2] != -1: return dp[idx1][idx2]
        if word1[idx1] == word2[idx2]:
            dp[idx1][idx2] = 0 + self.recursion(idx1-1,idx2-1,word1,word2,dp)
            return dp[idx1][idx2]
        dp[idx1][idx2] = min(
            1 + self.recursion(idx1-1,idx2,word1,word2,dp),
            1 + self.recursion(idx1,idx2-1,word1,word2,dp)
            )
        return dp[idx1][idx2]


    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2 = len(word1),len(word2)
        dp = [[-1 for i in range(n2)]for j in range(n1)]
        return self.recursion(n1-1,n2-1,word1,word2,dp)
        