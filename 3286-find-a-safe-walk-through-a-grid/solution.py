from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        
        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])
        
        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]
        
        while dq:
            r, c = dq.popleft()
            
            for i in range(4):
                nr = r + drow[i]
                nc = c + dcol[i]
                
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        
                        if cost == 0:
                            dq.appendleft((nr, nc)) 
                        else:
                            dq.append((nr, nc))    
        return health - dist[m-1][n-1] >= 1