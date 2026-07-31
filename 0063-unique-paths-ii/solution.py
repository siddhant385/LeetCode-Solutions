class Solution:
    def solveByRecursion(self,r,c,grid,dp):
        if (r,c) == (0,0):
            return 1
        if r < 0 or c < 0:
            return 0
        elif grid[r][c] ==1:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        dp[r][c] =  self.solveByRecursion(r,c-1,grid,dp) + self.solveByRecursion(r-1,c,grid,dp)
        return dp[r][c]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[-1 for i in range(cols)] for _ in range(rows)]
        return self.solveByRecursion(rows-1,cols-1,obstacleGrid,dp)
        