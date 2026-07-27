class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def ops_to_target(nums, target):
            arr = nums[:]
            ops = 0
            n = len(arr)
            for i in range(n - 1):
                if arr[i] != target:
                    arr[i] *= -1
                    arr[i + 1] *= -1
                    ops += 1
            if arr[-1] != target:
                return float('inf')
            return ops
    
        need1 = ops_to_target(nums, 1)
        need_1 = ops_to_target(nums, -1)
    
        return min(need1, need_1) <= k

            