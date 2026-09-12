class Solution:
    def recursion(self,i,j,s,p,dp):
        # both gets exhausteed return True
        if i<0 and j < 0:
            return True
        # if i is exhausted and j is remaining
        if j < 0 and i >= 0:
            return False
        if i < 0 and j >=0:
            for i in range(j+1):
                if p[i] != "*":
                    return False
            return True

        if dp[i][j] != -1:
            return dp[i][j]
        elif s[i] == p[j] or p[j] == "?":
            dp[i][j] = self.recursion(i-1,j-1,s,p,dp)
        elif p[j] == "*":
            dp[i][j] = self.recursion(i-1,j,s,p,dp) or self.recursion(i,j-1,s,p,dp)
        else:
            dp[i][j] = False
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[-1 for i in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j == 0:
                    dp[i][j] = True
                # if i is exhausted and j is remaining
                elif j == 0 and i > 0:
                    dp[i][j] = False
                elif i == 0 and j >0:
                    dp[i][j] = True
                    for x in range(j):
                        if p[x] != "*":
                            dp[i][j] = False
                elif s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[m][n]
                

        # return self.recursion(m-1,n-1,s,p,dp)
        