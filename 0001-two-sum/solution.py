class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx,i in enumerate(nums):
            if target-i in mp:
                return [idx,mp[target-i]]
            mp[i] = idx
            