class Solution:

    def recursion(self,i,j,s,t,dp):
        # return no of ways to generate subsequence
        if j <0:
            return 1
        if i <0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i] == t[j]:
            dp[i][j] = self.recursion(i-1,j-1,s,t,dp) + self.recursion(i-1,j,s,t,dp)
        else:
            dp[i][j]=self.recursion(i-1,j,s,t,dp)
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        m= len(s)
        n=len(t)
        dp=[[0 for i in range(n+1)]for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i ==0 and j ==0:
                    dp[i][j] = 1
                    continue
                if i==0:
                    dp[i][j] = 0
                    continue
                if j == 0:
                    dp[i][j] = 1
                    continue
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]


        # return self.recursion(m-1,n-1,s,t,dp)        