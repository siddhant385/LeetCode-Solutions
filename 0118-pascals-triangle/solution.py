class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            srow = []
            for j in range(i+1):
                if j ==0 or j==i:
                    srow.append(1)
                    continue
                else:
                    srow.append(res[i-1][j-1]+res[i-1][j])
            res.append(srow)
        return res

                

        