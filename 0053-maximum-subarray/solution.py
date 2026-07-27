class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        sums = 0
        for i in nums:
            sums += i
            max_sum = max(sums,max_sum)
            if sums < 0:
                sums = 0
            
        return max_sum
        