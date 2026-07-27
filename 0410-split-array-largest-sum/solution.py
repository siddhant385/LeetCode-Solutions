class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        res = right
        while left<=right:
            mid = left +(right - left) //2
            if self.canSplit(mid,nums,k):
                res = mid
                right = mid -1
            else:
                left = mid+1
        return res
    
    def canSplit(self,mid,nums,k):
        subarray = 1
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > mid:
                subarray +=1
                curSum = n
        return subarray <= k


        