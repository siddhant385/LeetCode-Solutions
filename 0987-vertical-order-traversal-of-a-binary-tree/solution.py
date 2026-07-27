# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([[root,0]])
        dc = dict()
        r = 0
        while q:
            n = len(q)
            for i in range(n):
                val = q.popleft()
                dc[val[1]] = dc.get(val[1],[])
                if dc[val[1]] == []:
                    dc[val[1]] = [(r,val[0].val)]
                else:
                    dc[val[1]].append((r,val[0].val))
                if val[0].left: q.append([val[0].left,val[1]-1])
                if val[0].right: q.append([val[0].right,val[1]+1])
            r+=1
        ans = []
        for key in sorted(dc.keys()):
            dc[key].sort()
            lst = []
            for i in dc[key]:
                lst.append(i[1])
            ans.append(lst)
        return ans





        