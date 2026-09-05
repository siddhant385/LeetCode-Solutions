class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxNum = float("-inf")
        n = len(nums)
        maxArr = []
        for i in range(n):
            maxNum = max(nums[i],maxNum)
            maxArr.append(maxNum)
        minNum = float("inf")
        minArr = []
        for j in range(n-1,-1,-1):
            minNum = min(nums[j],minNum)
            minArr.append(minNum)
        ans = 0
        for i in range(n):
            if maxArr[i] - minArr[n-i-1] <= k:
                return i
        return -1 


            

        