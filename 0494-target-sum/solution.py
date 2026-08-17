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

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-2 for _ in range(-2000,2001)]for _ in range(n)]
        return self.recursion(n-1,target,nums,dp)
        