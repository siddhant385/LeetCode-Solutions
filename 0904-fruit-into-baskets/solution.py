class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r = 0,0
        ans = 0
        fs = {}
        while r <len(fruits):
            fs[fruits[r]] = fs.get(fruits[r],0)+1
            if len(fs.keys()) > 2:
                if fs[fruits[l]] >0:
                    fs[fruits[l]] -=1
                if fs[fruits[l]] == 0:
                    fs.pop(fruits[l])
                l+=1
            r+=1
            ans = max(ans,r-l)
        return ans

        