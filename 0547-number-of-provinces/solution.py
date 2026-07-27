class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in range(n):
                if isConnected[node][i] == 1:
                    dfs(i)
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt +=1
                dfs(i)
        return cnt

        