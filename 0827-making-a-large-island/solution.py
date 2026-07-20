class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,i,j):
        absi = self.find(i)
        absj = self.find(j)
        if absi != absj:
            if self.rank[absi] < self.rank[absj]:
                self.parent[absi] = absj
            elif self.rank[absi]> self.rank[absj]:
                self.parent[absj] = absi
            else:
                self.parent[absi] = absj
                self.rank[absj] += 1
            return True
        return False
    def unionBySize(self,i,j):
        absi = self.find(i)
        absj = self.find(j)
        if absi != absj:
            if self.size[absi] < self.size[absj]:
                self.parent[absi] = absj
                self.size[absj] += self.size[absi]
            else:
                self.parent[absj] = absi
                self.size[absi] += self.size[absj]
            return True
        return False

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dsu = DSU(rows*cols)
        dr = [1,0,-1,0]
        dc = [0,1,0,-1]
        lsum = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                for i in range(4):
                    newr = r + dr[i]
                    newc = c + dc[i]
                    if -1<newr<rows and -1<newc<cols and grid[newr][newc] == 1:
                        dsu.unionBySize(cols*r+c,cols*newr+newc)
        
        has_zero = False
        for r in range(rows):
            for c in range(cols):
                sizeset = set()
                sumcheck = 0
                if grid[r][c] == 0:
                    has_zero = True
                    for i in range(4):
                        newr = r + dr[i]
                        newc = c + dc[i]
                        if -1<newr<rows and -1<newc<cols and grid[newr][newc] == 1:
                                sizeset.add(dsu.find(cols*newr+newc))
                sumcheck = 1 + sum(dsu.size[root] for root in sizeset)
                lsum = max(lsum,sumcheck)
        
        if not has_zero:
            return rows*cols
        
        return lsum

                            
                        


        

        



            


        