class Solution:
    def recursion(self,idx1,idx2,word1,word2,dp):
        if idx1 <0 or idx2<0:
            if idx1 < 0:
                return idx2+1
            else:
                return idx1+1
        if dp[idx1][idx2] != -1: return dp[idx1][idx2]
        if word1[idx1] == word2[idx2]:
            dp[idx1][idx2] = 0 + self.recursion(idx1-1,idx2-1,word1,word2,dp)
            return dp[idx1][idx2]
        dp[idx1][idx2] = min(
            1 + self.recursion(idx1-1,idx2,word1,word2,dp),
            1 + self.recursion(idx1,idx2-1,word1,word2,dp)
            )
        return dp[idx1][idx2]


    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2 = len(word1),len(word2)
        prev = [0 for i in range(n2+1)]
        for i in range(n1+1):
            curr = [0 for i in range(n2+1)]
            for j in range(n2+1):
                if i == 0:
                    curr[j] = j
                elif j ==0:
                    curr[j] = i
                
                elif word1[i-1] == word2[j-1]:
                    curr[j] = 0 + prev[j-1]
                else:
                    curr[j] = min(
                        1 + prev[j],
                        1 + curr[j-1]
                    )
            prev = curr
        return prev[n2]



        # return self.recursion(n1-1,n2-1,word1,word2,dp)
        