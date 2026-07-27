class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        # first lets find the max and min digit range out of the following loops
        # we will use nested for loop and an array to solve this
        hmp = defaultdict(list)
        for idx,num in enumerate(nums):
            max_num = float('-inf')
            min_num = float('inf')
            while num > 0:
                digit = num%10
                max_num = max(max_num,digit)
                min_num = min(min_num,digit)
                num = num //10
            hmp[max_num-min_num].append(idx)
        max_diff = max(hmp)
        ans = 0
        for values in hmp.get(max_diff):
            ans += nums[values]
        return ans
            
            
            
                
                
        