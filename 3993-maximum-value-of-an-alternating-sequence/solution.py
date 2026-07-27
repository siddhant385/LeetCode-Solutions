class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n ==1:
            return s
        k = (n-2) // 2
        return s + (k+1) * m-k