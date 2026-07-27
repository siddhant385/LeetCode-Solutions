class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        ans = 0
        al = {}
        for i in words:
            if len(i) <k:
                continue
            chr = i[:k]
            al[chr] = al.get(chr,0) + 1

        keys =al.keys()
        for j,i in enumerate(al.values()):
            if i >1:
                ans +=1
        return ans
                
        