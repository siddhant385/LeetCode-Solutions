class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()
        def helper(target):
            if target <= 0:
                if target ==0:
                    return 1
                return 0
            elif dp.get(target,None) != None:
                return dp[target]
            else:
                dp[target] = helper(target-1) + helper(target-2)
            return dp[target]
        return helper(n)
        