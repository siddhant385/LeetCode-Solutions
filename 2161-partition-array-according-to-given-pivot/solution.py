class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_nums = []
        greater_nums = []
        middle_nums = []
        for i in nums:
            if i < pivot:
                less_nums.append(i)
            elif i > pivot:
                greater_nums.append(i)
            else:
                middle_nums.append(i)
            
        return less_nums+middle_nums+greater_nums
        