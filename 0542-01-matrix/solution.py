class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = deque([])
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))
        d_row = [0,1,0,-1]
        d_col = [1,0,-1,0]
        count = 0
        while q:
            no_of_ele = len(q)
            for i in range(no_of_ele):
                r,c = q.popleft()
                if mat[r][c] == 1 and (r,c):
                    mat[r][c] = count
                for i in range(4):
                    row_to_add = r+d_row[i]
                    col_to_add = c+d_col[i]
                    if -1 < row_to_add <m and -1 < col_to_add < n and (row_to_add,col_to_add) not in visited:
                        q.append((row_to_add,col_to_add))
                        visited.add((row_to_add,col_to_add))
            count +=1
        return mat





        