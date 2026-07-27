class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:return False
        if (n - 1) & n ==0: return True
        return False
        