class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self,node):
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

        Dx = DSU(len(stones))
        # creating graph
        cnt = 0
        for i in range(len(stones)):
            x1,y1 = stones[i] #(0,0)
            for j in range(i+1,len(stones)):
                x2,y2 = stones[j] # (0,1)
                if x1==x2 or y1==y2:
                    if Dx.union(i,j):
                        cnt +=1
        return cnt

        