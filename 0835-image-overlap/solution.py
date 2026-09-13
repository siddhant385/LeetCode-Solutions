class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m = len(img1)
        n = len(img2)

        img1loc = set()
        img2loc = set()

        
        for i in range(m):
            for j in range(m):
                if img1[i][j] == 1:
                    img1loc.add((i,j))
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    img2loc.add((i,j))
        
        has = dict()
        for i in img1loc:
            for j in img2loc:
                cal = (i[0]-j[0],i[1]-j[1])
                has[cal] = has.get(cal,0) + 1
        ans = 0
        for i in has:
            ans = max(has[i],ans)
        return ans
            
        
