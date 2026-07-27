class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # let's collect elements which are acyclic
        # lets first create a visited array
        n = len(graph)
        visited = [0 for _ in range(n)]
        # we will use dfs so lets create a dfs recursive function
        def dfs(node):
            # we will mark this element as visited
            visited[node] = 1
            for nodes in graph[node]:
                # if it's 1 it means that we got the cycle
                if visited[nodes] == 1:
                    return False
                # if we have already processed the node then continue
                if visited[nodes] == 2:
                    continue
                # it means we have to perform dfs here
                if visited[nodes] == 0:
                    if not dfs(nodes):
                        return False
            # if we have done changing 
            visited[node] = 2
            return True
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
        return [i for i in range(n) if visited[i] == 2]
        




        