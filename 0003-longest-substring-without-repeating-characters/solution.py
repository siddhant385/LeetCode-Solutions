class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        sw = set()
        ans = 0
        while r < n:
            while s[r] in sw:
                sw.remove(s[l])
                l+=1
            sw.add(s[r])
            r+=1
            ans = max(ans, r-l)

        return ans

        