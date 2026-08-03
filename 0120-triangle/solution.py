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
        return self.SolveByRecursion(0,0,triangle,rows-1,dp)

        