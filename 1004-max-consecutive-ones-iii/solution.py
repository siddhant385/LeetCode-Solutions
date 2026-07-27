class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 0,0
        ans = 0
        while r <n:
            while k ==0 and nums[r]==0:
                if nums[l] == 0:
                    k +=1
                l +=1
            if nums[r] == 0:
                k-=1
            r +=1
            ans = max(ans, r-l)
        return ans

        