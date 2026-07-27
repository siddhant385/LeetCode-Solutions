class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Step 1 we will find the 1's in the matrix
        r,c = len(mat),len(mat[0])
        rc = [0]*r
        cc = [0]*c
        ans = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    cc[j] +=1
                    rc[i] +=1
        for i in range(r):
            for j in range(c):
                if mat[i][j] ==1 and rc[i]+cc[j] ==2:
                    ans +=1
        return ans


        
                


            



        