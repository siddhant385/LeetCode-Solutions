class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            l,r = 0,0
            ans = 0
            freq = {}
            while r < len(nums):
                freq[nums[r]] = freq.get(nums[r],0) +1
                while len(freq) > k:
                    freq[nums[l]] -=1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l +=1
                r+=1
                ans += r-l
            return ans
        return helper(k) - helper(k-1)


        