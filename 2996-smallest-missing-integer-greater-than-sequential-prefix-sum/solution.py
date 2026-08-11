class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        pointer = 1
        startSum = nums[0]
        while pointer < n and nums[pointer-1] + 1 == nums[pointer]:
            startSum += nums[pointer]
            pointer +=1
            print(pointer)
        hashSet = set()
        for i in nums:
            hashSet.add(i)
        
        while True:
            if startSum not in hashSet:
                return startSum
            startSum +=1
            
        


        