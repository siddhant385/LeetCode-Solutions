class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dn = {}
        ans = 0
        for num in nums:
            dn[num] = dn.get(num,0) +1
        for num in dn:
            if num+1 in dn:
                ans = max(ans,dn[num] + dn[num+1])
        return ans
        