class Solution:
    def recursion(self,r1,c1,c2,grid,rows,cols,dp):
        if cols-1 <c1 or c1 <0 or cols-1 < c2 or c2 < 0:
            return float('-inf')
        if r1 == rows-1:
            if c1 == c2:
                return grid[r1][c1]
            return grid[r1][c1] + grid[r1][c2]
        # Explore all the paths
        if dp[r1][c1][c2] != -1:
            return dp[r1][c1][c2]
        dp[r1][c1][c2] = 0
        for col1 in range(-1,2):
            for col2 in range(-1,2):
                if c1==c2:
                    dp[r1][c1][c2] = max(dp[r1][c1][c2],grid[r1][c1] + self.recursion(r1+1,c1-col1,c2-col2,grid,rows,cols,dp))
                else:
                    dp[r1][c1][c2] = max(dp[r1][c1][c2],grid[r1][c1]+ grid[r1][c2] + self.recursion(r1+1,c1-col1,c2-col2,grid,rows,cols,dp))
        return dp[r1][c1][c2]



    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        return self.recursion(0,0,cols-1,grid,rows,cols,dp)
        