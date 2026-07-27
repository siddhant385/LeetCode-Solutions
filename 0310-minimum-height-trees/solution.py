class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=2:
            return [i for i in range(n)]
        graph = defaultdict(list)
        for edge in edges:
            u,v = edge
            graph[u].append(v)
            graph[v].append(u)
        indegree = [0 for _ in range(n)]
        # giving degrees to our indegree
        for node in graph:
            indegree[node] = len(graph[node])
        # now we will use bfs on indegree
        # let's initailize queue
        q = deque()
        # lets add starting elements to queue
        for node,degree in enumerate(indegree):
            if degree == 1:
                q.append(node)
                node -=1
                # we subtract node by 1 as we have already pushed it into the array
        # from here bfs starts
        # if queue is empty or indegree becomes less than 3 then we have to stop our bfs
        while n >2:
            length = len(q)
            n-= length
            for i in range(length):
                node = q.popleft()
                for nodes in graph.get(node):
                    indegree[nodes] -=1
                    if indegree[nodes] ==1:
                        q.append(nodes)
        return list(q)
                
                

                
        
            
        