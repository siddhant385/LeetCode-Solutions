class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = list()
        lst = ["a","b","c"]
        def helper(s,nb):
            lg = len(s)
            if len(ans) > k:
                return

            if lg == n:
                ans.append("".join(s[:]))
                return
            elif lg > n:
                return
            for i in range(3):
                if i == nb:
                    continue
                s.append(lst[i])
                helper(s,i)
                s.pop()
        helper([],-1)
        if len(ans) < k:
            return ""
        return ans[k-1]