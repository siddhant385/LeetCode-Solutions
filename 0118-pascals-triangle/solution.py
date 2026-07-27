class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows+1):
            srow = []
            for j in range(i):
                if j ==0 or j==i-1:
                    srow.append(1)
                    continue
                srow.append(res[i-2][j-1]+res[i-2][j])
            if srow!= []:res.append(srow)
        return res

                

        