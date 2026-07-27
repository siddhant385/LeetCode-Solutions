class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l,r = 0,0
        cnt = {}
        ans = 0
        while (r<n):
            cnt[s[r]] = cnt.get(s[r],0) +1
            mv = max(cnt.values()) 
            while (r-l +1) - mv > k:
                cnt[s[l]] -=1
                l+=1
            r +=1
            ans = max(ans ,r-l)
        
        return ans


        