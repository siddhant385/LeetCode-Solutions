class Solution:
    def rob(self, nums: List[int]) -> int:
        def findrob(n,nums):
            prev = nums[0]
            prev2 = 0
            curr = 0
            for i in range(1,n):
                pick = nums[i]
                if i > 1:
                    pick += prev2
                notPick = 0 + prev
                curr = max(pick,notPick)
                prev2 = prev
                prev = curr
            return prev
        # taking 1st element and removing last
        n = len(nums)
        if n ==1:
            return nums[0]
        first = nums[:n]
        # removing first and taking last
        last = nums[1:]
        return max(findrob(n-1,first),findrob(n-1,last))