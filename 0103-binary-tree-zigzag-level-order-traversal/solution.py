# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []
        s = 0
        if not root:
            return ans
        while q:
            lst = []
            n = len(q)
            for i in range(n):
                v = q.popleft()
                if v.right: q.append(v.right)
                if v.left: q.append(v.left)
                lst.append(v.val)

            if s%2==0:
                ans.append(lst[::-1])
            else:
                ans.append(lst)
            s+=1
        return ans





        