class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # create pq
        pq = []
        heapq.heappush(pq,(0,0,(0,0)))
        drow = [1,0,-1,0]
        dcol = [0,1,0,-1]
        while pq:
            obs_removed,value,cordinates = heapq.heappop(pq)
            r,c = cordinates
            # already 2 continue
            if grid[r][c] == 2: continue
            # mark the grid value as 2 
            grid[r][c] = 2
            # if we found our path
            if cordinates == (m-1,n-1):
                return obs_removed
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if -1 < nrow < m and -1 < ncol < n and grid[nrow][ncol] !=2:
                    newObsremoved = obs_removed
                    if grid[nrow][ncol] == 1:
                        newObsremoved += 1
                    heapq.heappush(pq,(newObsremoved,grid[nrow][ncol],(nrow,ncol)))
        



        