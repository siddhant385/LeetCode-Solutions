class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prefix_sum = 0
        ans = 0
        for i in range(n - 1):
            val = nums[i]
            prefix_sum += val
            suffix_sum = total - prefix_sum
            remaining_count = n - 1 - i
            if val * remaining_count > suffix_sum:
                ans += 1   
        return ans