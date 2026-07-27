class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        l1 = float('inf')
        l2 = float('inf')
        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] == 1:
                l1 = i
                ans = min(ans, abs(l1-l2))

            if nums[i] == 2:
                l2 = i
                ans = min(ans, abs(l1-l2))
        if ans == float('inf'):
            return -1
        return ans
            
            
                
                
                
        