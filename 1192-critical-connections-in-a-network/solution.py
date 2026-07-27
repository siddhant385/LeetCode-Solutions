class Solution:
    def __init__(self):
        self.timer = 1
    def dfs(self,node,parent,vis,adj,tin,low,ans):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer +=1 
        for neighbours in adj[node]:
            if neighbours == parent:
                continue
            if vis[neighbours] == 0:
                self.dfs(neighbours,node,vis,adj,tin,low,ans)
                low[node] = min(low[node],low[neighbours])
                if low[neighbours] > tin[node]:
                    ans.append([neighbours,node])
            else:
                low[node] = min(low[node],tin[neighbours])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for edge1,edge2 in connections:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)
        vis = [0 for i in range(n)]
        tin = [0 for i in range(n)]
        low = [0 for i in range(n)]
        ans = []
        self.dfs(0,-1,vis,adj,tin,low,ans)
        return ans
        

        