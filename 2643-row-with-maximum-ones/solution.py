class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for row in range(len(mat)):
            cnt =0
            for i in mat[row]:
                if i ==1:
                    cnt+=1
            if ans[1] < cnt: ans = [row,cnt]
        return ans


        