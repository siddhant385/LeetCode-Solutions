class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ts = {0:1}
        ans = 0
        s = 0
        for i in nums:
            s += i
            if s - goal in ts:
                ans +=ts[s-goal]
            
            ts[s] = ts.get(s,0) +1
        return ans
            

        