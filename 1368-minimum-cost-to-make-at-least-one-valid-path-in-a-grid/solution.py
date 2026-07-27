class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 0 right 1 left 2 up 3 down
        drow = [0,0,1,-1]
        dcol = [1,-1,0,0]
        # we will give cost in bfs and do ingrid transformation
        pq = [] # create priority queue for cost 
        # pq structuree will be cost,row,col
        heapq.heappush(pq,(0,0,0))
        while pq:
            cost,r,c = heapq.heappop(pq)
            if grid[r][c] == 5:continue
            # we will give value of 5 to r,c as they are visited
            grid_value = grid[r][c]
            grid[r][c] = 5
            # if reached destination then return cost
            if (r,c) == (m-1,n-1):
                return cost
            nrow = r + drow[grid_value-1]
            ncol = c + dcol[grid_value-1]
            if -1 < nrow < m and -1 < ncol < n and grid[nrow][ncol] != 5:
                heapq.heappush(pq,(cost,nrow,ncol))
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if -1 < nrow < m and -1 < ncol < n:
                    heapq.heappush(pq,(cost+1,nrow,ncol))


        
        