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
        prev=[0 for i in range(n+1)]
        for i in range(m+1):
            curr=[0 for i in range(n+1)]
            for j in range(n+1):
                if i ==0 and j ==0:
                    curr[j] = 1
                    continue
                if i==0:
                    curr[j] = 0
                    continue
                if j == 0:
                    curr[j] = 1
                    continue
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1] + prev[j]
                else:
                    curr[j]=prev[j]
            prev = curr
        return prev[n]


        # return self.recursion(m-1,n-1,s,t,dp)        