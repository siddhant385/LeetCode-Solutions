class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        # def gcd(a,b):
        #     if a == 0:
        #         return b
        #     if a > b:
        #         a,b = b,a
        #     rem = b % a  
        #     return gcd(rem,a)
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                hcf = math.gcd(nums[i],nums[j])
                ans = max(ans,(nums[i] * nums[j]) // (hcf*hcf))
        return ans