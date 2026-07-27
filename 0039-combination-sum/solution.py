class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(s,target,i):
            add = sum(s)
            if add >= target or i < 0:
                if add==target:
                    ans.append(s[:])
                return 
            s.append(candidates[i])
            helper(s,target,i)
            s.pop()
            helper(s,target,i-1)
        helper([],target,len(candidates)-1)
        
        return ans