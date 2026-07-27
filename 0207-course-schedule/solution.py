class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating adjacency list
        if not prerequisites:
            return True
        mp = defaultdict(list)
        for u,v in prerequisites:
            mp[u].append(v)
        visited = dict()
        def dfs(node):
            visited[node] = 1
            for nbor in mp[node]:
                if nbor not in visited:
                    if not dfs(nbor):
                        return False
                elif visited[nbor] == 1:
                    return False
                    
            visited[node] = 2
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i): return False
        return True

        