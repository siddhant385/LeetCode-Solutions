class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorr = 0
        for i in nums:
            xorr = xorr^i
        r = xorr ^ (xorr & xorr-1)
        b1 = 0
        b2 = 0
        for i in nums:
            if r & i ==0:
                b1 = b1^i
            else:
                b2 = b2^i
        return [b1,b2]
        