class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        ans = []
        isInserted = False
        for i in intervals:
            if i[1] < newInterval[0]:
                ans.append(i)
            elif i[0] > newInterval[1]:
                if not isInserted:
                    ans.append(newInterval)
                    isInserted = True
                ans.append(i)
            else:
                lst = []
                lst.append(min(i[0],newInterval[0]))
                lst.append(max(i[1],newInterval[1]))
                newInterval = lst
        if not isInserted:
            ans.append(newInterval)   
        return ans


        