class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        lenr = len(grid)
        lenc = len(grid[0])
        # use bfs
        # initialize queue
        q = deque()
        # initialize visited set
        visited = set()
        # check if 0,0 is 0 if its 1 then return -1 else return add (0,0),0 in queue
        if grid[0][0] == 0:
            q.append(((0,0),1))
            visited.add((0,0))
        # if q isn't empty continue
        while q:
        # check its length
            n = len(q)
        # loop through queue elements
            for i in range(n):
        # popleft the elements and store distance and node
                node,distance = q.popleft()
        # if the node is final node then add +1 distnace and return the distance
                if node == (lenr-1,lenc-1):
                    return distance
                r,c = node
        # for all 8 directions check if the node isn't visited and contains 0 node then put the distance and the node on the queue mark the node as visited and continue
                drow = [1,-1,0,0,1,-1,1,-1]
                dcol = [0,0,1,-1,1,-1,-1,1]
                for i in range(8):
                    n_row = r + drow[i]
                    n_col = c + dcol[i]
                    if -1 < n_row < lenr and -1 < n_col < lenc and (n_row,n_col) not in visited and grid[n_row][n_col] == 0:
                        q.append(((n_row,n_col),distance+1))
                        visited.add((n_row,n_col))
        # at last return -1 if no node is found
        return -1


        