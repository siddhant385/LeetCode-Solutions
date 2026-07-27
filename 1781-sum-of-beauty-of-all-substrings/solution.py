class Solution:
    def beautySum(self, s: str) -> int:
        subarray = []
        res = 0
        for i in range(len(s)):
            array = []
            stng = s[i]
            
            for j in range(i+1,len(s)):
                stng+=s[j]
                freq = {}
                if len(stng) > 2:
                    for ch in stng:
                        freq[ch] = freq.get(ch,0) +1
                    res += freq[max(freq,key=freq.get)] - freq[min(freq,key=freq.get)]
        return res

        