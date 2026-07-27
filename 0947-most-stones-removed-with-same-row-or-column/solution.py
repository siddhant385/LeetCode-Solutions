class DSU:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
    
    def find(self,node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0
            
        if self.parent[node] == node:
            return node
            
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,i,j):
        abs_i = self.find(i)
        abs_j = self.find(j)
        if abs_i != abs_j:
            if self.rank[abs_i] < self.rank[abs_j]:
                self.parent[abs_i] = abs_j
            elif self.rank[abs_i] > self.rank[abs_j]:
                self.parent[abs_j] = abs_i
            else:
                self.parent[abs_i] = abs_j
                self.rank[abs_j] += 1
            return True
        return False
        

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        Dx = DSU()
        # creating graph
        cnt = 0
        for i in stones:
            x = i[0]
            y = pow(10,4) + i[1] +1
            Dx.union(x,y)
        total_leaders = 0
        for node in Dx.parent:
            if Dx.parent[node] == node:
                total_leaders += 1
        return n - total_leaders
        