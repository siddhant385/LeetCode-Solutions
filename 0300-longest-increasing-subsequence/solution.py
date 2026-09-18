class Solution:
    def recursion(self,i,prev,nums,dp):
        if i == len(nums):
            return 0
        if dp[i][prev+1] != -2:
            return dp[i][prev+1]
        dp[i][prev+1] = 0 + self.recursion(i+1,prev,nums,dp)
        if prev == -1 or nums[i] > nums[prev]:
            dp[i][prev+1] = max(dp[i][prev+1],1 + self.recursion(i+1,i,nums,dp))
        return dp[i][prev+1]
        
        return max(pick,notPick)
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        maxi = 1
        for i in range(n):
            for prev in range(0,i):
                if nums[prev] < nums[i]:
                    dp[i] = max(1+dp[prev],dp[i])
            maxi = max(maxi,dp[i])
        return maxi

        