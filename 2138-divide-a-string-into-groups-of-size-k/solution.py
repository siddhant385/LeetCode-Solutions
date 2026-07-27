class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        toadd = length % k
        if toadd != 0:
            toadd = k-toadd
        res = []
        for i in range(0,length,k):
            res.append(s[i:i+k:])
        for i in range(toadd):
            res[-1]+=fill
        return res
        