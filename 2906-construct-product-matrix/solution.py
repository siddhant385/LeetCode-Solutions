class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)
        
        size = n * m
        
        prefix = [1] * size
        suffix = [1] * size
        
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        res = []
        idx = 0
        
        for i in range(n):
            row = []
            for j in range(m):
                val = (prefix[idx] * suffix[idx]) % MOD
                row.append(val)
                idx += 1
            res.append(row)
        
        return res