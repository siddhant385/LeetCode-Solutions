class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row = 0
        col = cols - 1
        count = 0
        while (row < rows and col > -1): 
            if grid[row][col] < 0:
                count += ( rows-row)                 
                col -= 1
            else:
                row +=1
        return count
                