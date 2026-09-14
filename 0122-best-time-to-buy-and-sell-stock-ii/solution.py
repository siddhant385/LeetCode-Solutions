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
        dp = [[-1 for i in range(2)]for i in range(n)]
        return self.recursion(0,True,prices,dp)

        