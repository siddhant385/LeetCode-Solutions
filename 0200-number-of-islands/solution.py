class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # store the 1's present in the water
        ones = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ones.add((i,j))
        
        def isIland(q):
            drow = [1,0,-1,0]
            dcol = [0,1,0,-1]
            while q:
                r,c = q.popleft()
                for i in range(4):
                    nrow = r+drow[i]
                    ncol = c+dcol[i]
                    if -1<nrow<m and -1<ncol<n and grid[nrow][ncol]!="0" and (nrow,ncol) in ones:
                        ones.remove((nrow,ncol))
                        q.append((nrow,ncol))
            return 1
        ans = 0
        while ones:
            q = deque()
            q.append(ones.pop())
            ans += isIland(q)
        return ans

        