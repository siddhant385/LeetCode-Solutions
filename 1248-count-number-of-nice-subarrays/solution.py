class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # [1,1,0,1,1] nums
        def atmost(ko):
            l,r = 0,0
            s = 0
            cnt = 0
            if ko < 0:
                return 0
            while r < len(nums):
                s += nums[r]%2
                while s > ko:
                    s -= nums[l]%2
                    l +=1
                if s <= ko:cnt += r-l+1
                r += 1
            return cnt
                    

        return atmost(k) - atmost(k-1)