class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        f = 0
        s = 0
        while f<len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s +=1
            f +=1
        return s


        