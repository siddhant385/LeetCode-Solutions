class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        mf = 1
        csum =nums[0]
        l = 0
        r = 0
        while l <= r and r < len(nums):
            size = (r - l)+1
            total = size * nums[r]
            print(r)
            if total - csum <= k:
                r+=1
                if r<len(nums):
                    csum += nums[r]
                mf = max(mf,size)
            else:
                csum -= nums[l]
                l+=1
                
        return mf




        