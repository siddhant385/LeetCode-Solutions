class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        mp = {}
        i = n
        while i !=0:
            num = i % 10
            mp[num] = mp.get(num,0) +1
            i = i // 10
        ans = 0
        for i in mp:
            ans += i * mp[i]
        return ans
            
        