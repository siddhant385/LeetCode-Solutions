class Solution:
    def recursion(self,idx,target,nums,dp):
        # base case
        if target == 0:
            return True
        if idx ==0:
            return nums[idx] == target
        
        if dp[idx][target] != -1:
            return dp[idx][target]
        
        not_choose = self.recursion(idx-1,target,nums,dp)
        choose = self.recursion(idx-1,target-nums[idx],nums,dp)
        dp[idx][target] =  choose or not_choose
        return dp[idx][target]

        # main logic return true or false
    def canPartition(self, nums: List[int]) -> bool:
        sumofNumber = sum(nums)
        if sumofNumber %2 != 0: return False
        target = sumofNumber //2
        n = len(nums)
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        return self.recursion(n-1,target,nums,dp)


        