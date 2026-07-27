class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        p = 1
        q = 0
        ans = 0
        while p < len(intervals):
            if intervals[q][1] > intervals[p][0]:
                if intervals[q][1] > intervals[p][1]:
                    q = p
                ans +=1
                p +=1
            else:
                q = p
                p+=1
        return ans

            
        