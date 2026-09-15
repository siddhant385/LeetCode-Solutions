class Solution:
    def recursion(self,i,buy,prices,dp):
        if i >= len(prices):
            return 0
        if dp[i][buy] != -1:
            return dp[i][buy]
        if buy:
            dp[i][buy] = max(-prices[i] + self.recursion(i+1,False,prices,dp),0+self.recursion(i+1,True,prices,dp))
        else:
            dp[i][buy] = max(prices[i]+ self.recursion(i+1,True,prices,dp),0+self.recursion(i+1,False,prices,dp))
        return dp[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(2)]for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j:
                    dp[i][j] = max(-prices[i] + dp[i+1][0],0+dp[i+1][1])
                else:
                    dp[i][j] = max(prices[i]+ dp[i+1][1],0+dp[i+1][0])
        return dp[0][1]
        # return self.recursion(0,True,prices,dp)

        