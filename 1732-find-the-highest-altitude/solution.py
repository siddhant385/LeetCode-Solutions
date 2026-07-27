class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        z=0
        for i in gain:
            z +=i
            ans = max(z,ans)
        return ans





        