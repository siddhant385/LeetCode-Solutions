class Solution:
    def compare(self,w1,w2):
        lw1 = len(w1)
        lw2 = len(w2)
        if lw1 != lw2 +1:
            return False
        p1 = 0
        p2 = 0
        while p1 < lw1:
            if p2 < lw2 and w1[p1] == w2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        if p1 == lw1 and p2 == lw2:
            return True
        

    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key = len)
        maxi = 1
        n = len(words)
        dp = [1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if self.compare(words[i],words[j]):
                    dp[i] = max(dp[i],dp[j] +1)
            
            maxi = max(maxi,dp[i])
        
        return maxi
        
                
        