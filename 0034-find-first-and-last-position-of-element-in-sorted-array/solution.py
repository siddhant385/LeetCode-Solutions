class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right- left) //2
            if nums[mid] == target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        if left >=len(nums):
            return [-1,-1]
        if nums[left] != target:
            return [-1,-1]
        res.append(left)
        right = len(nums)-1
        left = 0
        while left <= right:
            mid = left + (right- left) //2
            if nums[mid] == target:
                left = mid +1
            elif nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
        res.append(left-1)
        return res
        