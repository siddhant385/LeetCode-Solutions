class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        if not occupiedIntervals:
            return []
            
        occupiedIntervals.sort()
        ot = []
        lst = occupiedIntervals[0]
        
        for p in range(1, len(occupiedIntervals)):
            if occupiedIntervals[p][0] <= lst[1] + 1:
                lst[1] = max(lst[1], occupiedIntervals[p][1])
            else:
                ot.append(lst)
                lst = occupiedIntervals[p]
        ot.append(lst)
        
        ans = []
        for i in ot:
            if i[1] < freeStart or i[0] > freeEnd:
                ans.append(i)
            else:
                if i[0] <= freeStart - 1:
                    ans.append([i[0], freeStart - 1])
                if freeEnd + 1 <= i[1]:
                    ans.append([freeEnd + 1, i[1]])
                    
        return ans
            
            
            
                
                
        
                
                
            
        
        