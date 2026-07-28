class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        dp = [float('-inf') for _ in range(len(nums))]
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        # for i in range(2,n):
        #     pick = nums[i] + dp[i-2]
        #     notPick = 0 + dp[i-1]
        #     dp[i] = max(pick,notPick)
        # return dp[-1]



        def helper(idx):
            if idx == 0:
                return nums[idx]
            elif idx <0:
                return 0
            if dp[idx] != float("-inf"):
                return dp[idx]
            else:
                pick = nums[idx] + helper(idx-2)
                notPick = 0 + helper(idx-1)
                dp[idx] = max(pick,notPick)
            return dp[idx]
        ans = helper(len(nums)-1)
        return ans
