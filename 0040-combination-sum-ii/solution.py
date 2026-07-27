class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        candidates.sort()
        def helper(s,index):
            add = sum(s)
            # here we will write based condtion
            # we'll stop when add == target or index < len(candidates)
            if add > target:
                return
            if add == target:
                ans.append(s[:])
            
            for i in range(index,len(candidates)):
                if candidates[i] == candidates[i-1] and i > index:
                    continue
                s.append(candidates[i])
                helper(s,i+1)
                s.pop()
            
        # We will call our function recursively here
        helper([],0)
        return ans


        