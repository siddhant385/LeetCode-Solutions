class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1,nums2=set(nums1),set(nums2)
        freq = dict()
        for i in nums1:
            freq[i] = freq.get(i,0) + 1
        for j in nums2:
            freq[j] = freq.get(j,0) + 1
        print(freq)
        for fre in freq:
            if freq[fre] > 1:
                if fre in nums1:
                    nums1.remove(fre)
                if fre in nums2:
                    nums2.remove(fre)
        return [list(nums1),list(nums2)]      