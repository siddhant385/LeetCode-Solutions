class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Getting zeros connected to boundary
        m = len(board)
        n = len(board[0])
        q = []
        non_convertible = set()
        for row in range(m):
            if row == 0:
                for col in range(n):
                    if board[row][col] == "O":
                        q.append((row,col))
                        non_convertible.add((row,col))
            elif row ==m-1:
                for col in range(n):
                    if board[row][col] == "O":
                        q.append((row,col))
                        non_convertible.add((row,col))
            else:
                if board[row][0] == "O":
                    q.append((row,0))
                    non_convertible.add((row,0))
                
                if board[row][n-1] == "O":
                    print(board[row][n-1])
                    q.append((row,n-1))
                    non_convertible.add((row,n-1))
        # Using stack to find the neigbors connected to the boundary
        d_row = [1,0,-1,0]
        d_col = [0,1,0,-1]
        while q:
            r,c = q.pop()
            non_convertible.add((r,c))
            for i in range(4):
                row = r+d_row[i]
                col = c+d_col[i]
                if 0 < row < m-1 and 0< col< n-1 and (row,col) not in non_convertible and board[row][col] == "O":
                    q.append((row,col))
        for r in range(m):
            for c in range(n):
                if (r,c) not in non_convertible and board[r][c] == "O":
                    board[r][c] = "X"
        


        

                

