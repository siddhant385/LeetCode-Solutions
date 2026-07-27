# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        ans = []
        if not root:
            return ans
        while q:
            n = len(q)
            flag = True
            for i in range(n):
                v = q.popleft()
                if flag:
                    ans.append(v.val)
                    flag = False
                if v.right:q.append(v.right)
                if v.left:q.append(v.left)
        return ans


        