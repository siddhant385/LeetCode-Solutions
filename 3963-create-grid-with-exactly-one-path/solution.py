class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # create a m*n grid
        ans = []
        for i in range(m):
            if i ==0:
                lst = "."*n
            else:
                lst = "#"*(n-1) + "."
            ans.append(lst)
        return ans
            
        
                
        