class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        vis = set()
        fresh = 0
        # finding rotten oranges in the matrix
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:fresh+=1
                if grid[i][j] ==2:
                    q.append((i,j,0))
                    vis.add((i,j))
        # performing bfs
        d_row = [1,0,-1,0]
        d_col = [0,1,0,-1]
        time = 0
        rotted = 0
        while q:
            r,c,t = q.popleft()
            for i in range(4):
                row = r+d_row[i]
                col = c+d_col[i]
                if -1 < row<n and -1<col<m and grid[row][col] ==1 and (row,col) not in vis:
                    q.append((row,col,t+1))
                    rotted +=1
                    vis.add((row,col))
            time = max(time, t)
        # checking if all fresh tomatoes are rotten
        if rotted != fresh:
            return -1
        return time
        
        



        