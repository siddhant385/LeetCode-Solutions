class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        while left<=right:
            mid = left+(right-left)//2
            hours = self.banacheck(mid, piles)
            if hours<=h:
                right = mid -1
            elif hours>h:
                left = mid+1
        return left
    
    def banacheck(self,mid,piles):
        sum = 0
        for i in piles:
            sum += ceil(i/mid)
        return sum
            
        
        