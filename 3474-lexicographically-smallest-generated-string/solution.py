class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        word = ['?'] * L
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i+j] != '?' and word[i+j] != str2[j]:
                        return ""
                    word[i+j] = str2[j]
                    
        satisfied = [False] * n
        last_empty = [-1] * n
        
        for i in range(n):
            if str1[i] == 'F':
                is_sat = False
                last_e = -1
                for j in range(m):
                    if word[i+j] == '?':
                        last_e = i + j
                    elif word[i+j] != str2[j]:
                        is_sat = True
                        break
                if is_sat:
                    satisfied[i] = True
                else:
                    if last_e == -1:
                        return ""
                    last_empty[i] = last_e
                    satisfied[i] = False
                    
        for k in range(L):
            if word[k] != '?':
                continue
            
            prohibited = set()
            start_i = max(0, k - m + 1)
            end_i = min(n - 1, k)
            
            for i in range(start_i, end_i + 1):
                if str1[i] == 'F' and not satisfied[i]:
                    if last_empty[i] == k:
                        prohibited.add(str2[k - i])
                        
            chosen = ''
            for ascii_val in range(97, 123):
                c = chr(ascii_val)
                if c not in prohibited:
                    chosen = c
                    break
                    
            if not chosen:
                return ""
                
            word[k] = chosen
            
            for i in range(start_i, end_i + 1):
                if str1[i] == 'F' and not satisfied[i]:
                    if chosen != str2[k - i]:
                        satisfied[i] = True
                        
        return "".join(word)