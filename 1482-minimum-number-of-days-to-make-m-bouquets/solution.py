class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1
        while left<=right:
            mid = left + (right-left) //2
            if self.isfine(mid,k,m,bloomDay):
                right = mid-1
                ans = mid
            else:
                left = mid +1
        return ans


    
    def isfine(self,mid,k,m,bloomDay):
        adjacent = 0
        boquet = 0
        for i in bloomDay:
            if i <= mid:
                adjacent+=1
            if adjacent == k:
                boquet +=1
                adjacent=0
            if i > mid:
                adjacent = 0
        return boquet >= m
