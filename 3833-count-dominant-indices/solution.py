class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total = sum(nums)
        minus = 0
        ans = 0
        for i in range(len(nums)-1):
            minus +=nums[i]
            a = total-minus
            b = len(nums)-(i+1)
            print(a,b)
            if nums[i] > a/b:
                ans +=1
        return ans



        