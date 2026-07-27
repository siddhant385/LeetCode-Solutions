class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countmap = {0:1}
        count = 0
        presum = 0
        for num in nums:
            presum += num
            if (presum-k) in countmap:
                count+= countmap[presum-k]
            countmap[presum] = countmap.get(presum, 0) + 1
        return count

            



        