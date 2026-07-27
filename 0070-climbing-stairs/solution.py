class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev = 1
        count = 0
        for i in range(2,n+1):
            count = prev + prev2
            prev2 = prev
            prev = count
        return prev
        