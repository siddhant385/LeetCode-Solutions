class Solution:
    def recursion(self,idx,target,coins,dp):
        if idx <0:
            return 0
        if target == 0:
            return 1
        if dp[idx][target] != -1:
            return dp[idx][target]
        pick = 0
        if coins[idx] <= target:
            pick = self.recursion(idx,target-coins[idx],coins,dp)
        notPick = self.recursion(idx-1,target,coins,dp)
        dp[idx][target] = pick + notPick
        return dp[idx][target]
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)]for _ in range(n)]
        return self.recursion(n-1,amount,coins,dp)

        