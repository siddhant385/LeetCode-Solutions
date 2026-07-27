class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1,nums2 = set(nums1),set(nums2)
        freq = dict()
        for i in nums1:
            freq[i] = freq.get(i,0)+1
        
        for j in nums2:
            freq[j] = freq.get(j,0)+1
        ans = []
        for i in freq:
            if freq[i] > 1:
                ans.append(i)
        return ans


        