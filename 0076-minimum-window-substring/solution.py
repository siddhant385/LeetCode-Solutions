class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        window = {}
        
        have = 0
        need = len(count_t) 
        
        res = [-1, -1] 
        resLen = float("inf")
        
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in count_t and window[char] == count_t[char]:
                have += 1
                
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                    
                left += 1
                
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""