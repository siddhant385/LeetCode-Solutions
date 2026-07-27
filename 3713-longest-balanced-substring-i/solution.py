class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        n = len(s)
        if n ==1: return 1
        for i in range(n):
            hm = {}
            hm[s[i]] = hm.get(s[i],0) +1
            for j in range(i+1,n):
                hm[s[j]] = hm.get(s[j],0) +1
                lhmv = hm.values()
                if len(set(lhmv)) == 1:
                    ans = max(ans,j-i+1)
        return ans