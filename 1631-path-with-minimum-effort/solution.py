class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        # iss question ko solve krne ke liye hum modified djikstra use krenge
        # hum sabse pehle ek priority q bnate h 
        effort_matrix = [[float('inf') for _ in range(n)] for _ in range(m)]
        pq = []
        # ab isme apan 0,0 ko daalte h 
        # humara pq hoga wo difference ke hisab se priority setup krega
        heapq.heappush(pq,(0,0,0))
        effort_matrix[0][0] = 0
        # ab yha se start krte h 
        drow = [1,0,-1,0]
        dcol = [0,1,0,-1]
        while pq:
            effort,r,c = heapq.heappop(pq)
            if (r,c) == (m-1,n-1):
                return effort
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if -1<nrow<m and -1<ncol<n:
                    new_effort = max(abs(heights[nrow][ncol]-heights[r][c]),effort)
                    if new_effort < effort_matrix[nrow][ncol]:
                        effort_matrix[nrow][ncol] = new_effort
                        heapq.heappush(pq,(new_effort,nrow,ncol))
        return effort


            

        