class Solution:
    # def SolveByRecursion(self,row,col,grid):
    #     if (row,col) == (0,0):
    #         return grid[row][col]
    #     if row < 0 or col < 0:
    #         return float('inf')
    #     right = grid[row][col] + self.SolveByRecursion(row,col-1,grid)
    #     up = grid[row][col] + self.SolveByRecursion(row-1,col,grid)
    #     return min(up,right)
    # def SolveByMemoization(self,row,col,grid,dp):
    #     if (row,col) == (0,0):
    #         return grid[row][col]
    #     if row < 0 or col < 0:
    #         return float('inf')
    #     if dp[row][col] != -1:
    #         return dp[row][col]
    #     right = grid[row][col] + self.SolveByMemoization(row,col-1,grid,dp)
    #     up = grid[row][col] + self.SolveByMemoization(row-1,col,grid,dp)
    #     dp[row][col] = min(up,right)
    #     return dp[row][col]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1 for i in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if (row,col) == (0,0):
                    dp[row][col] = grid[row][col]
                else:
                    right,up = float('inf'),float('inf')
                    if col > 0:
                        right = grid[row][col] + dp[row][col-1]
                    if row > 0:
                        up = grid[row][col] + dp[row-1][col]
                    dp[row][col] = min(up,right)

        return dp[rows-1][cols-1]
        