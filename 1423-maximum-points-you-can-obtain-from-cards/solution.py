class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        ans = 0
        rsum = 0
        r = 1
        n = len(cardPoints)
        for i in range(k):
            lsum += cardPoints[i]   
        ans = lsum
        for j in range(k-1,-1,-1):
            lsum -= cardPoints[j]
            rsum += cardPoints[n-r]
            r+=1
            ans = max(ans,lsum+rsum)
        return ans

            
                 
        