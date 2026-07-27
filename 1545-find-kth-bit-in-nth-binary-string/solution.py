class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        mid = 2 ** (n - 1)
        if k == mid:
            return "1" 
        elif k < mid:
            return self.findKthBit(n - 1, k)            
        else:
            new_k = (2 ** n) - k
            res = self.findKthBit(n - 1, new_k)
            return "0" if res == "1" else "1"