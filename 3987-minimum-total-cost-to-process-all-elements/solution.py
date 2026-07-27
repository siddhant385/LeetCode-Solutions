class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        tempK = k
        cost = 0
        num = 0
        for i in range(len(nums)):
            if nums[i] <=tempK:
                tempK = tempK - nums[i]
            else:
                jump = ((nums[i] - tempK) + k - 1) // k
                tempK = k * jump + tempK - nums[i]
                newnum = num+jump
                cost += (newnum*(newnum+1))//2 - (num*(num+1))//2
                num = newnum
        return cost % (10**9+7)
                
        