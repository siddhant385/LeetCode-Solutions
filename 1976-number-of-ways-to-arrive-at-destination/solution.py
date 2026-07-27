class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # lets first create adjacency matrix node -> (time,dest)
        MAX = 10**9 + 7
        graph = defaultdict(list)
        for src,dest,time in roads:
            graph[src].append((time,dest))
            graph[dest].append((time,src))
        # This is our array it will contain shortest distance 
        time_array = [float('inf') for _ in range(n)]
        ways = [0 for _ in range(n)]
        # lets append our first value in priority queue but lets setup first
        pq = []
        # we have given time,dest
        heapq.heappush(pq,(0,0))
        time_array[0] = 0
        ways[0] = 1
        while pq:
            time,dest = heapq.heappop(pq)
            # if we got the shortest path
            
            for neighbor_time,neighbor in graph[dest]:
                # here we are going for the first time so we will put our way for first time
                if time_array[neighbor] > time+neighbor_time:
                    time_array[neighbor] = time+neighbor_time
                    ways[neighbor] = ways[dest]
                    heapq.heappush(pq,(time+neighbor_time,neighbor))
                elif time_array[neighbor] == time+neighbor_time:
                    ways[neighbor] += ways[dest]
        return ways[n-1] % MAX


        