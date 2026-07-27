class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # lets create our adjacency graph first
        # we will store answer as a list such that first will be city and second will be number
        ans = [float('inf'),float('inf')]
        graph = defaultdict(list)
        for u,v,dist in edges:
            graph[u].append((dist,v))
            graph[v].append((dist,u))
        # lets create a distance matrix
        for src in range(n):
            dist = [float('inf') for _ in range(n)]
            # lets create a priority queue
            pq = []
            # lets push our source node in priority queue (dist,src)
            heapq.heappush(pq,(0,src))
            # also change dist to 0
            dist[src] = 0
            # Now lets use while loop for djikstra
            while pq:
                # pop the first element
                node_dist,node = heapq.heappop(pq)
                for distance,neighbors in graph[node]:
                    if dist[neighbors] > distance + dist[node]:
                        dist[neighbors] = distance+dist[node]
                        heapq.heappush(pq,(distance+dist[node],neighbors))
            th = 0
            
            for cities in dist:
                if cities <= distanceThreshold:
                    th+=1
            if ans[1] >= th:
                ans[0] = src
                ans[1] = th
        return ans[0]

            


        