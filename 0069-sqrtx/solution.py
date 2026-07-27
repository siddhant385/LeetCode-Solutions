class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        left = 1
        right = (x//2)**2
        ans = 1
        while left<=right:
            mid = left + (right-left)//2
            square = mid*mid
            if square <= x:
                ans = mid
                left = mid+1
            if square > x:
                right = mid -1
        return ans

        