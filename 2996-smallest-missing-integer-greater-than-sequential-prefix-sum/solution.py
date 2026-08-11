class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        pointer = 1
        startSum = nums[0]
        while pointer < n and nums[pointer-1] + 1 == nums[pointer]:
            startSum += nums[pointer]
            pointer +=1
            print(pointer)
        hash = set()
        for i in nums:
            hash.add(i)
        
        for i in range(startSum,1276):
            if i not in hash:
                return i
        


        