class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # This walkable_cell will contain row column
        walkable_cells = set()
        st = []
        m = len(grid)
        n = len(grid[0])
        # loop for finding walkable cells in boundary
        for j in range(n):
            if grid[0][j] == 1:
                st.append((0,j))
                walkable_cells.add((0,j))
            if grid[m-1][j] == 1:
                st.append((m-1,j))
                walkable_cells.add((m-1,j))
        for i in range(1,m-1):
            if grid[i][0] == 1:
                st.append((i,0))
                walkable_cells.add((i,0))
            if grid[i][n-1] ==1:
                st.append((i,n-1))
                walkable_cells.add((i,n-1))
        
        
        # traversing the outuer boundaries using stack traversal
        while st:
            # remove value from stack
            r,c = st.pop()

            # check if there left right up down exists as 1 and check if they already are not in walkable_cells
            d_row = [1,0,-1,0]
            d_col = [0,1,0,-1]
            for i in range(4):
                row = r+d_row[i]
                col = c+d_col[i]
                if -1 < row < m and -1 < col < n and grid[row][col] == 1 and (row,col) not in walkable_cells:
                    # add them to both stack and visited
                    st.append((row,col))
                    walkable_cells.add((row,col))
            
        # Now we have to do just check no. of 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in walkable_cells and grid[i][j] == 1:
                    ans+=1
        return ans

               
