class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        product = float("-inf")
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    if nums[i] != nums[j]:
                        if product < nums[i] * nums[j]:
                            product = nums[i] * nums[j]
                            if nums[i] > nums[j]:
                                ans = [i,j]
                            elif nums[i] < nums[j]:
                                ans = [j,i]


        if ans == []:
            return [-1,-1]
        return ans
                    
                    
                
            
            
        