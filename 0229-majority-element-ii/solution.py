class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = dict()
        for i in nums:
            d[i] = d.get(i,0) +1
        ans = []
        for k in d:
            if d[k] > n/3:
                ans.append(k)
        return ans
        
        