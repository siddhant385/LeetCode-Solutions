class Solution:
    def recursion(self,idx,target,coins,dp):
        if idx <=0:
            if idx == 0:
                if target % coins[idx] == 0:
                    return target // coins[idx]
                else:
                    return float('inf')
            return 0
        
        if dp[idx][target] != -2:
            return dp[idx][target]

        notPick = 0 + self.recursion(idx-1,target,coins,dp)
        pick = float('inf')
        if coins[idx] <= target:
            pick = 1 + self.recursion(idx,target-coins[idx],coins,dp)
        dp[idx][target] =  min(pick,notPick)
        return dp[idx][target]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        prev = [-2 for _ in range(amount+1)]
        for i in range(amount+1):
            if i % coins[0] == 0:
                    prev[i] = i // coins[0] 
            else:
                prev[i] = float('inf')
        
        for i in range(1,n):
            for target in range(amount+1):
                notPick = 0 + prev[target]
                pick = float('inf')
                if coins[i] <= target:
                    pick = 1 + prev[target-coins[i]]
                prev[target] =  min(pick,notPick)
                

        return -1 if prev[amount] == float("inf") else prev[amount]


        # return -1 if self.recursion(n-1,amount,coins,dp) == float('inf') else self.recursion(n-1,amount,coins,dp)

        