class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        left = {c: s.find(c) for c in set(s)}
        right = {c: s.rfind(c) for c in set(s)}
        
        def get_valid_right(i):
            right_bound = right[s[i]]
            j = i
            
            while j <= right_bound:
                if left[s[j]] < i:
                    return -1
                right_bound = max(right_bound, right[s[j]])
                j += 1
                
            return right_bound

        intervals = []
        for i in range(len(s)):
            if i == left[s[i]]:
                new_right = get_valid_right(i)
                if new_right != -1:
                    intervals.append((i, new_right))
                    
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        last_end = -1
        
        for start, end in intervals:
            if start > last_end:
                res.append(s[start:end+1])
                last_end = end
                
        return res
        