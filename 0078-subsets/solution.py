class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = (1 << n)
        ans = []
        for i in range(subset):
            l = []
            for j in range(n):
                if i & (1 << j):
                    l.append(nums[j])
            ans.append(l)
        return ans



        