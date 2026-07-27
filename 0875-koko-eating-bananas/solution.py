class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        while left<=right:
            mid = left+(right-left)//2
            if self.banacheck(mid,piles)<=h:
                right = mid -1
            elif self.banacheck(mid,piles)>h:
                left = mid+1
        return left
    
    def banacheck(self,mid,piles):
        sum = 0
        for i in piles:
            sum += ceil(i/mid)
        return sum
            
        
        