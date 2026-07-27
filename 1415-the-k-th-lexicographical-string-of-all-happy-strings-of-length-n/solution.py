class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = list()
        lst = ["a","b","c"]
        def helper(s,nb,c):
            lg = len(s)
            if lg == n:
                ans.append("".join(s[:]))
                c +=1
                return
            elif lg > n or c > k:
                return
            for i in range(3):
                if i == nb:
                    continue
                s.append(lst[i])
                helper(s,i,c)
                s.pop()
        helper([],-1,0)
        if len(ans) < k:
            return ""
        return ans[k-1]