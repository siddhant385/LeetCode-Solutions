class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        left = 1
        right = max(position)
        ans = 0
        while left<=right:
            mid = left + (right-left)//2
            res = self.isForce(mid,position,m)
            if res:
                ans = mid
                left =mid +1
            else:
                right = mid-1
        return ans
    def isForce(self,mid,position,m):
        cur = 1
        position.sort()
        last_pos = position[0]
        for i in range(1,len(position)):
            if position[i] - last_pos >=mid:
                cur+=1
                last_pos = position[i]
            if cur>=m:
                return True
        return False


            

        