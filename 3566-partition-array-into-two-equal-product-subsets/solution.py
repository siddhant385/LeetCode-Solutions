class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        all_elements_mask = (1 << n) - 1
        valid_subsets = []

        # Find all subsets with product == target
        for mask in range(1, 1 << n):
            prod = 1
            for i in range(n):
                if (mask >> i) & 1:
                    prod *= nums[i]
                    if prod > target:
                        break
            if prod == target:
                valid_subsets.append(mask)

        # Check pairs of valid subsets for:
        # 1) disjointness
        # 2) union covers all elements
        for i in range(len(valid_subsets)):
            for j in range(i + 1, len(valid_subsets)):
                mask1 = valid_subsets[i]
                mask2 = valid_subsets[j]
                if (mask1 & mask2) == 0 and (mask1 | mask2) == all_elements_mask:
                    return True
        return False
