class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        curr_char = 'a'
        
        for i in range(n):
            if word[i] == '':
                if curr_char > 'z':
                    return ""
                
                word[i] = curr_char
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = curr_char
                        
                curr_char = chr(ord(curr_char) + 1)
                
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                actual_lcp = 0
                if word[i] == word[j]:
                    actual_lcp = 1 + (lcp[i+1][j+1] if i + 1 < n and j + 1 < n else 0)
                
                if actual_lcp != lcp[i][j]:
                    return ""
                    
        return "".join(word)