class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    # find absolute parent method
    def find(self,node):
        if self.parent[node] == node:
            return node
        else:
            # agar parent[node] ka koi aur parent h 
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node] 
    
    def union(self,nodeA,nodeB):
        absParentOfNodeA = self.find(nodeA)
        absParentOfNodeB = self.find(nodeB)
        if absParentOfNodeA != absParentOfNodeB:
            if self.rank[absParentOfNodeA] < self.rank[absParentOfNodeB]:
                self.parent[absParentOfNodeA] = absParentOfNodeB
            elif self.rank[absParentOfNodeA] > self.rank[absParentOfNodeB]:
                self.parent[absParentOfNodeB] = absParentOfNodeA
            else:
                self.parent[absParentOfNodeA] = absParentOfNodeB
                self.rank[absParentOfNodeB] +=1
            return True
        else:
            return False
    



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        length_of_connections = len(connections)
        # impossible -1
        if length_of_connections < n-1:
            return -1
        uf = DSU(n)
        for u, v in connections:
            uf.union(u, v)
        total_groups = 0
        for i in range(n):
            if uf.parent[i] == i:
                total_groups += 1                
        return total_groups - 1