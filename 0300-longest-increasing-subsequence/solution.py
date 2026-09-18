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
        dp = [[-2 for i in range(n+1)]for _ in range(n)]
        return self.recursion(0,-1,nums,dp)
        