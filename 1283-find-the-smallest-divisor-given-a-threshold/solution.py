class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = -1
        while left <=right:
            mid = left +(right-left) //2
            condition = self.sumquot(mid,nums)
            if condition <= threshold:
                ans = mid
                right = mid-1
            if condition > threshold:
                left = mid+1
        return ans
            
            

    def sumquot(self,mid,nums):
        sum = 0
        for i in nums:
            sum += ceil(i /mid)
        return sum

        