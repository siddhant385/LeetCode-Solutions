class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        n = len(nums)
        ts = 0
        for i in range(k):
            if mul > 0:
                ts += nums[n-1] * mul
            else:
                ts += nums[n-1]
            mul -=1
            n -=1

        return ts
            