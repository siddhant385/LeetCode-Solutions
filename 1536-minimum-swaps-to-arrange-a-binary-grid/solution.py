class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        trailing = [row[::-1].index(1) if 1 in row else n for row in grid]
        
        swaps = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and trailing[j] < need:
                j += 1
            if j == n:
                return -1
            swaps += j - i
            trailing[i:j+1] = [trailing[j]] + trailing[i:j]
        return swaps