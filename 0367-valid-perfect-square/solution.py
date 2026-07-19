class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        l = 1
        r = num //2
        while l <=r:
            mid = (l+r)//2
            if num / mid == mid:
                return True
            elif num / mid < mid:
                r = mid-1
            elif num / mid > mid:
                l = mid+1
        return False

        