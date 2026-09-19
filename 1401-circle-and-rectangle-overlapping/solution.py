class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xclosest = max(x1,min(xCenter,x2))
        yclosest = max(y1,min(yCenter,y2))
        if pow(xclosest-xCenter,2) + pow(yclosest-yCenter,2) > pow(radius,2):
            return False
        return True
            


        
        