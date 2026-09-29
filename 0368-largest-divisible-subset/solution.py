class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        hasha = [0 for i in range(n)]
        dp = [1 for i in range(n)]
        maxi = 1
        lastIndex = 0
        for i in range(1,n):
            hasha[i] = i
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] +1
                    hasha[i] = j
            
            if dp[i] > maxi:
                maxi = dp[i]
                lastIndex = i
        temp = list()
        temp.append(nums[lastIndex])
        while(hasha[lastIndex] != lastIndex):
            lastIndex = hasha[lastIndex]
            temp.append(nums[lastIndex])
        return temp[::-1]

        