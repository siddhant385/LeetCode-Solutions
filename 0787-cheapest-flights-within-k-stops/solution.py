class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # lets start question by making adjacency graph
        graph = defaultdict(list)
        for start,to,price in flights:
            graph[start].append((price,to))
        # lets create a priority queue it will contain (price,k,src)
        pq = []
        # lets create a k_price_array this will contain only price
        k_price = [float('inf') for i in range(n)]
        # lets put our src in pq
        heapq.heappush(pq,(0,0,src))
        k_price[src] = 0
        while pq:
            # lets remove src from priority queue
            pk,price,src = heapq.heappop(pq)
            new_k = pk+1
            if new_k > k+1:
                continue
            for route_price,routes in graph[src]:
                if k_price[routes] > price+route_price:
                    k_price[routes] = price+route_price
                    heapq.heappush(pq,(new_k,price+route_price,routes))
        
        if k_price[dst] == float('inf'):
            return -1
        else:
            return k_price[dst]
                

                



        

        