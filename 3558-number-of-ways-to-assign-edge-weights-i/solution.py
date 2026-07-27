class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        tree = {}
        for i in edges:
            if i[0] not in tree:
                tree[i[0]] = []
            tree[i[0]].append(i[1])
            if i[1] not in tree:
                tree[i[1]] = []
            tree[i[1]].append(i[0])

        max_depth = [0]
        def dfs(current_element,parent,depth):
            max_depth[0] = max(max_depth[0],depth)
            for neighbor in tree[current_element]:
                if neighbor != parent:
                    dfs(neighbor,current_element,depth+1)
        dfs(1,-1,0)
        return pow(2, max_depth[0] - 1, 10**9 + 7)
                    
                
                
        