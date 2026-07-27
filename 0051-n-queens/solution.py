class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        posdig = set()
        negdig = set()
        lin = set()
        
        def backtracking(r,c,board,q):
            if q == n:
                ans.append(board[:])
                return
            
            for i in range(n):
                if i in lin:
                    continue
                if r-i in posdig or r+i in negdig:
                    continue
                board.append(("." * i) + "Q" + ("." * (n - 1 - i)))
                lin.add(i)
                posdig.add(r-i)
                negdig.add(r+i)
                backtracking(r+1,i,board,q+1)
                negdig.remove(r+i)
                posdig.remove(r-i)
                lin.remove(i)
                board.pop()

        backtracking(0,0,[],0)
        return ans