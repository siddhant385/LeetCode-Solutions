class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(s,target,i):
            if sum(s) >= target or i < 0:
                if sum(s)==target:
                    ans.append(s[:])
                return 
            s.append(candidates[i])
            helper(s,target,i)
            s.pop()
            helper(s,target,i-1)
        helper([],target,len(candidates)-1)
        
        return ans