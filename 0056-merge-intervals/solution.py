class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        p = 1
        ans = [intervals[0]]
        while p < n:
            if ans[-1][1] >= intervals[p][0]:
                ans[-1][1] = max(ans[-1][1], intervals[p][1])
            else:
                ans.append(intervals[p])
            p+=1
                
        return ans
        