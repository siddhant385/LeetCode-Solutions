class Solution:
    def recursion(self,idx1,idx2,text1,text2):
        # this function will return the max length of subsequences
        if idx1 <0 or idx2 < 0:
            return 0
        if text1[idx1] == text2[idx2]:
            return 1 + self.recursion(idx1-1,idx2-1,text1,text2)
        return max(self.recursion(idx1-1,idx2,text1,text2) , self.recursion(idx1,idx2-1,text1,text2))
    
    def memoization(self,idx1,idx2,text1,text2,dp):
        # this function will return the max length of subsequences
        if idx1 <0 or idx2 < 0:
            return 0
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        if text1[idx1] == text2[idx2]:
            dp[idx1][idx2] = 1 + self.memoization(idx1-1,idx2-1,text1,text2,dp)
            return dp[idx1][idx2]
        dp[idx1][idx2] = max(self.memoization(idx1-1,idx2,text1,text2,dp) , self.memoization(idx1,idx2-1,text1,text2,dp))
        return dp[idx1][idx2]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for i in range(n2+1)]for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1][n2]
            


        


        