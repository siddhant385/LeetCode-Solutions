class Solution:
    def recursion(self,i,buy,c,prices,dp):
        if i >= len(prices) or c<=0:
            return 0
        if dp[i][buy][c] != -1:
            return dp[i][buy][c]
        if buy:
            dp[i][buy][c] = max(-prices[i] + self.recursion(i+1,False,c,prices,dp),self.recursion(i+1,True,c,prices,dp))
        else:
            dp[i][buy][c] = max(prices[i] + self.recursion(i+1,True,c-1,prices,dp),self.recursion(i+1,False,c,prices,dp))
        return dp[i][buy][c]
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[-1 for i in range(3)]for _ in range(2)]for _ in range(n)]
        return self.recursion(0,True,2,prices,dp)