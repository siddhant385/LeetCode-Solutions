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
    
    def tabulation(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)]for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(n):
            for j in range(1,amount+1):
                pick = 0
                if coins[i] <= j:
                    pick = dp[i][j-coins[i]]
                notPick = 0
                if i -1 >= 0:
                    notPick = dp[i-1][j]
                dp[i][j] = pick + notPick
        return dp[n-1][amount]

    

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0 for _ in range(amount+1)]
        prev[0] = 1
        for i in range(n):
            curr = [0 for _ in range(amount+1)]
            curr[0] = 1
            for j in range(1,amount+1):
                pick = 0
                if coins[i] <= j:
                    pick = curr[j-coins[i]]
                notPick = 0
                if i -1 >= 0:
                    notPick = prev[j]
                curr[j] = pick + notPick
            prev = curr
        return prev[amount]



        # return self.recursion(n-1,amount,coins,dp)

        