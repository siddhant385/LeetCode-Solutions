class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def helper(s,t,idx):
            sz = len(s)
            if t==n and sz==k:
                ans.append(s[:])
                return
            if t>n or sz==k:
                return
            for i in range(idx,10):
                t+=i
                s.append(i)
                helper(s,t,i+1)
                s.pop()
                t-=i
        helper([],0,1)
        return ans
                

        