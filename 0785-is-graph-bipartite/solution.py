class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        numOfNodes = len(graph)
        visited = dict()
        def dfs(node,color):
            visited[node] = color
            for i in graph[node]:
                if color == 0:n_color = 1
                else:n_color=0
                visited_color = visited.get(i,None)
                if visited_color == n_color:
                    continue
                elif visited_color is not None:
                    return False
                else:
                    if not dfs(i,n_color):
                        return False
            return True
        for i in range(numOfNodes):
            if i not in visited:
                if not dfs(i,0):
                    return False
        return True
                
        