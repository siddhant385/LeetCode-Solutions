class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            l,r = 0,0
            s = 0
            cnt = 0
            if goal <0: return 0

            while r < len(nums):
                s += nums[r]
                while s > goal:
                    s -= nums[l]
                    l +=1
                cnt += r-l +1
                r +=1
            
            return cnt
        return atmost(goal) - atmost(goal-1)

            

        