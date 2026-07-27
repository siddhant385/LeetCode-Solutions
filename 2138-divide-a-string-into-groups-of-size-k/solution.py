class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        toadd = length % k
        res = []
        if toadd != 0:
            s += fill * (k - toadd)
        for i in range(0,length,k):
            res.append(s[i:i+k:])
        return res
        