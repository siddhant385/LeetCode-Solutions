class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = []
        for i in grid:
            c = 0
            for j in range(len(i)):
                if i[n-1-j] == 0:
                    c+=1
                else:
                    break
            count.append(c)
        ans = 0
        for i in range(n):
            req = n-1-i
            idx = -1
            for j in range(i,n):
                if count[j] >=req:
                    idx = j
                    break
            if idx == -1:
                return idx
            for k in range(j,i,-1):
                ans +=1
                tmp = count[k-1]
                count[k-1] = count[k]
                count[k] = tmp
        return ans