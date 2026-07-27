class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l,r = 0,m*n-1
        while l<=r:
            mid = l + (r-l)//2
            val = matrix[mid//n][mid%n]
            print(mid,val)
            if val < target:
                l = mid+1
            elif val > target:
                r = mid-1
            else:
                return True
        return False

        