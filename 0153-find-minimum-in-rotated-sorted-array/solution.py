class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) -1
        min_num = nums[0]
        while left<=right:
            mid = left + (right - left) //2 
            if nums[mid] >= nums[left]:
                min_num = min(nums[left],min_num)
                left = mid +1
            elif nums[mid] < nums[right]:
                min_num = min(nums[mid],min_num)
                right = mid -1
        return min_num

        