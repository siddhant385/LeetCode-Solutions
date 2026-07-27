class Solution:
    def maxDistance(self, moves: str) -> int:
        x,y = 0,0
        mtm = 0
        for i in moves:
            if i == "L":
                x -=1
            elif i == "R":
                x +=1
            elif i == "U":
                y +=1
            elif i == "D":
                y -=1
            else:
                mtm +=1
        ans = abs(x) + abs(y)
        for i in range(mtm):
            ans +=1
        return ans
            
            
                
                
                
                
            
    
        