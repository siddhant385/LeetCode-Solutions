class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        p = n
        bits = 0
        while (p>0):
            p = p >>1
            bits +=1
        ms = (1 << bits) - 1
        return ms ^ n

         
        