class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        s = 0
        for i in range(m - 1):
            s += sum(grid[i])
            if s * 2 == total:
                return True
        
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        
        s = 0
        for j in range(n - 1):
            s += col_sums[j]
            if s * 2 == total:
                return True
        
        return False