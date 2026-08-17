class Solution:
    def recursion(self,idx,target,nums,dp):
        """This function will return no of ways we get a target"""
        if idx == 0:
            if nums[0] == 0 and target == 0:
                return 2
            if nums[0]+target == 0 or nums[0]-target == 0:
                return 1
            return 0
        if dp[idx][target+2000] != -2:
            return dp[idx][target+2000]
        pickPlus = self.recursion(idx-1,target-nums[idx],nums,dp)
        pickMinus = self.recursion(idx-1,target+nums[idx],nums,dp)
        dp[idx][target+2000] = pickPlus + pickMinus
        return dp[idx][target+2000]
    
    def tabulation(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if abs(target) > total_sum: 
            return 0
        dp = [[0 for _ in range(-2000,2001)]for _ in range(n)]
        dp[0][nums[0] + 2000] += 1
        dp[0][-nums[0] + 2000] += 1
        for i in range(1,n):
            for j in range(-total_sum,total_sum+1):
                pickPlus = dp[i-1][j+2000-nums[i]]
                pickMinus = dp[i-1][j+2000+nums[i]]
                dp[i][j+2000] = pickPlus + pickMinus

        return dp[n-1][target+2000]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if abs(target) > total_sum: 
            return 0
        prev = [0 for _ in range(-2000,2001)]
        prev[nums[0] + 2000] += 1
        prev[-nums[0] + 2000] += 1
        for i in range(1,n):
            curr = [0 for _ in range(-2000,2001)]
            for j in range(-total_sum,total_sum+1):
                pickPlus = prev[j+2000-nums[i]]
                pickMinus = prev[j+2000+nums[i]]
                curr[j+2000] = pickPlus + pickMinus
            prev = curr

        return prev[target+2000]
        # return self.recursion(n-1,target,nums,dp)
        