class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # creating adjacency matrix
        graph = defaultdict(list)
        n = len(quiet)
        for i in range(n):
            graph[i] = []
        for rich in richer:
            isRich,isPoor = rich[0],rich[1]
            graph[isPoor].append(isRich)
        # We will use dfs here for checking the minimum quietness and returning the answer
        # we will initialize our array with -1 
        ans = [float('inf') for i in range(n)]
        def dfs(node):
            # Given a node
            min_node = node
            for rich_nodes in graph.get(node,[]):
                # we will check whether the ans array has infinte for given node or not
                if ans[rich_nodes] == float('inf'):
                    # here we are getting node,quietness from the dfs recursion
                    found_node = dfs(rich_nodes)
                    if quiet[min_node] > quiet[found_node]:
                        min_node = found_node
                else:
                    if quiet[min_node] > quiet[ans[rich_nodes]]:
                        min_node = ans[rich_nodes]

            # once richest node is found
            # set its value for the answer
            ans[node] = min_node
            return min_node

        for i in range(n):
            if ans[i] == float("inf"):
                dfs(i)
        return ans

        

        