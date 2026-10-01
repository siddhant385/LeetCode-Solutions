class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        ans_idx = 0
        freq = [1 for i in range(n)]
        maxi = 1
        if len(set(nums)) == 1:
            return n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] +1
                        freq[i] = freq[j]
                    elif dp[i] == dp[j] +1:
                        freq[i] += freq[j]
            if maxi < dp[i]:
                maxi = dp[i]
                ans_idx = i
        
        ans = 0 
        for i in range(n):
            if dp[i] == maxi:
                ans +=freq[i]
        return ans

                
        
                

        