class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        c1 = 0
        c2 = 0
        ans = 0
        mod = 10**9+7
        for x in nums:
            if x< a:
                ans += c1 + c2
            elif x<=b:
                ans += c2
                c1 += 1
            else:
                c2 +=1
        return ans % mod
        
        