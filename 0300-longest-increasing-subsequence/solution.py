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
    def usingAlgorithmandforprinting(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        has = [1 for i in range(n)]
        maxi = 1
        lastIndex = 0
        for i in range(n):
            has[i] = i
            for prev in range(0,i):
                if nums[prev] < nums[i] and 1+dp[prev] > dp[i]:
                    dp[i] = 1+dp[prev]
                    has[i] = prev
            if dp[i] > maxi:
                maxi = dp[i]
                lastIndex = i
        lis = [0 for i in range(maxi)]
        lis[0] = nums[lastIndex]
        while has[lastIndex] != lastIndex:
            
            return maxi
    def lengthOfLIS(self, nums: list[int]) -> int:
        temp = [nums[0]]
        n = len(nums)
        ans = 1
        for i in range(n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                ans +=1
            else:
                idx = bisect.bisect_left(temp,nums[i])
                temp[idx] = nums[i]
        return ans