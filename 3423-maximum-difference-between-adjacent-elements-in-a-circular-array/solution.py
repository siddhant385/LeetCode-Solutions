class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        for i in range(0,len(nums)):
            if i == len(nums)-1:
                max_diff = max(abs(nums[i]-nums[0]),max_diff)
            else:
                max_diff = max(abs(nums[i] - nums[i+1]),max_diff)
            print(max_diff)
        return max_diff



        