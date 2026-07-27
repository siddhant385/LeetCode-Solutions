class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        if k == 0:
            return True
        
        for i, row in enumerate(mat):
            if i % 2 == 0:
                if row != row[k:] + row[:k]:
                    return False
            else:
                if row != row[-k:] + row[:-k]:
                    return False
                    
        return True