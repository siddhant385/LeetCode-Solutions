class Solution:
    def SolveByRecursion(self,row,col,triangle,n,dp):
        if row == n:
            return triangle[row][col]
        if dp[row][col] != float('inf'):
            return dp[row][col]
        down = triangle[row][col] + self.SolveByRecursion(row+1,col,triangle,n,dp)
        diagonal = triangle[row][col] + self.SolveByRecursion(row+1,col+1,triangle,n,dp)
        dp[row][col] = min(down,diagonal)
        return dp[row][col]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[float("inf") for _ in range(rows)] for _ in range(rows)]
        for i in range(rows):
            dp[rows-1][i] = triangle[rows-1][i]
        
        for i in range(rows-2,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,diagonal)
        return dp[0][0]



            
        
        # return self.SolveByRecursion(0,0,triangle,rows-1,dp)

        