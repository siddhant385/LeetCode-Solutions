from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        total = sum(row_sums)
        
        min_row, max_row = {}, {}
        min_col, max_col = {}, {}
        
        for r in range(m):
            for c in range(n):
                v = grid[r][c]
                if v not in min_row:
                    min_row[v] = r
                    max_row[v] = r
                    min_col[v] = c
                    max_col[v] = c
                else:
                    if r < min_row[v]: min_row[v] = r
                    if r > max_row[v]: max_row[v] = r
                    if c < min_col[v]: min_col[v] = c
                    if c > max_col[v]: max_col[v] = c
        
        s_top = 0
        for i in range(m - 1):
            s_top += row_sums[i]
            s_bot = total - s_top
            if s_top == s_bot:
                return True
            
            if s_top > s_bot:
                d = s_top - s_bot
                if n == 1:
                    if grid[0][0] == d or grid[i][0] == d: return True
                else:
                    if i == 0:
                        if grid[0][0] == d or grid[0][n-1] == d: return True
                    else:
                        if d in min_row and min_row[d] <= i: return True
            else:
                d = s_bot - s_top
                if n == 1:
                    if grid[i+1][0] == d or grid[m-1][0] == d: return True
                else:
                    if i == m - 2:
                        if grid[m-1][0] == d or grid[m-1][n-1] == d: return True
                    else:
                        if d in max_row and max_row[d] >= i + 1: return True

        s_left = 0
        for j in range(n - 1):
            s_left += col_sums[j]
            s_right = total - s_left
            if s_left == s_right:
                return True
            
            if s_left > s_right:
                d = s_left - s_right
                if m == 1:
                    if grid[0][0] == d or grid[0][j] == d: return True
                else:
                    if j == 0:
                        if grid[0][0] == d or grid[m-1][0] == d: return True
                    else:
                        if d in min_col and min_col[d] <= j: return True
            else:
                d = s_right - s_left
                if m == 1:
                    if grid[0][j+1] == d or grid[0][n-1] == d: return True
                else:
                    if j == n - 2:
                        if grid[0][n-1] == d or grid[m-1][n-1] == d: return True
                    else:
                        if d in max_col and max_col[d] >= j + 1: return True

        return False