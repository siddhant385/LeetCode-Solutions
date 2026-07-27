class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_nums = []
        greater_nums = []
        for i in nums:
            if i < pivot:
                less_nums.append(i)
            elif i > pivot:
                greater_nums.append(i)
        for i in nums:
            if i == pivot:
                less_nums.append(i)
        return less_nums+greater_nums
        