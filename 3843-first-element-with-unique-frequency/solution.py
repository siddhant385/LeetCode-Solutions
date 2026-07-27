class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i,0)+1
        val = hash.values()
        c_freq = {}
        for i in val:
            c_freq[i] = c_freq.get(i,0) +1
        for j in nums:
            if c_freq[hash[j]] ==1:
                return j
        return -1
            
            
        
        
            
            
        
        
        