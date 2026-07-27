class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1

        if s == 0:
            return 0

        ans = 0
        for _ in range(n):
            if s >=9:
                ans = ans * 10 + 9
                s-=9
            else:
                ans = ans * 10 + s
                s=0
        return ans
        
        