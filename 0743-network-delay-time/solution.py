class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # lets create an adjaceny list for the graph first
        graph = defaultdict(list)
        for src_node,dest_node,time in times:
            graph[src_node-1].append((time,dest_node-1))
        # lets now create priority queue
        pq = []
        # now lets create our min_timme array
        min_time = [float('inf') for i in range(n)]
        # now let's append our src node to pq along with time taken
        heapq.heappush(pq,(0,k-1))
        min_time[k-1] = 0
        while pq:
            time,node = heapq.heappop(pq)
            for neighbor_time,neighbor in graph[node]:
                if min_time[neighbor] > time+neighbor_time:
                    min_time[neighbor] = time+neighbor_time
                    heapq.heappush(pq,(time+neighbor_time,neighbor))
        ans = max(min_time)
        if ans == float('inf'): return -1
        else:return ans

        