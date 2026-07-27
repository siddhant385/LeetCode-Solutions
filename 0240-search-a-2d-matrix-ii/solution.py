class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row,col = 0,n-1
        while row < m and col >=0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -=1
            else:
                row+=1
        return False