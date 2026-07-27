class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        pq = []
        ans = float('-inf')
        heapq.heappush(pq,(grid[0][0],0,0))
        visited = [[0 for i in range(cols)] for i in range(rows)]
        dr = [1,0,-1,0]
        dc = [0,1,0,-1]
        while pq:
            weight,r,c = heapq.heappop(pq)
            ans = max(ans,weight)
            if (r,c) == (rows-1,cols-1):
                return ans
            if visited[r][c] == 1:
                continue
            visited[r][c] = 1
            for i in range(4):
                newr = r + dr[i]
                newc = c + dc[i]
                if -1<newr<rows and -1<newc<cols and visited[newr][newc] == 0:
                    
                    heapq.heappush(pq,(grid[newr][newc],newr,newc))
        return ans
