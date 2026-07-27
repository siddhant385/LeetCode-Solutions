class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def helper(s,idx):
            ans.append(s[:])
            for i in range(idx,len(nums)):
                if i>idx and nums[i]==nums[i-1]:continue
                s.append(nums[i])
                helper(s,i+1)
                s.pop()
            
        helper([],0)
        return ans

        