class Solution:
    def minFlips(self,s: str) -> int:
        n = len(s)
        s = s + s        
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += '1' if i % 2 == 0 else '0'
            alt2 += '0' if i % 2 == 0 else '1'
            
        diff1, diff2 = 0, 0
        min_flips = float('inf')        
        for i in range(len(s)):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1                
            if i >= n:
                left_index = i - n
                if s[left_index] != alt1[left_index]:
                    diff1 -= 1
                if s[left_index] != alt2[left_index]:
                    diff2 -= 1                    
            if i >= n - 1:
                min_flips = min(min_flips, diff1, diff2)
                
        return min_flips
        