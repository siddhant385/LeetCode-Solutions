class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        candidates.sort()
        def helper(s,index,add):
            # here we will write based condtion
            # we'll stop when add == target or index < len(candidates)
            if add < 0:
                return
            if add == 0:
                ans.append(s[:])
                return
            
            for i in range(index,len(candidates)):
                if candidates[i] == candidates[i-1] and i > index:
                    continue
                s.append(candidates[i])
                add -= candidates[i]
                helper(s,i+1,add)
                s.pop()
                add += candidates[i]
            
        # We will call our function recursively here
        helper([],0,target)
        return ans


        