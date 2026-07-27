class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        # using brute force for creating subarray
        n = len(nums)
        ans = 0
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += nums[j]
                digit = str(sum)
                if int(digit[0]) == x and int(digit[-1]) == x:
                    ans+=1
        return ans

                    
                    
                
        