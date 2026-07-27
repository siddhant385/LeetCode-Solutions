class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        minNum = intervals[0][0]
        maxNum =intervals[0][1]
        for lst in intervals:
            minNum = min(minNum,lst[0])
            if lst[0] > maxNum:
                res.append([minNum,maxNum])
                maxNum = lst[1]
                minNum = lst[0]

            elif lst[0] <= maxNum:
                maxNum = max(lst[1],maxNum)
        res.append([minNum,maxNum])
        return res



        