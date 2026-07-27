# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        qu = []
        ans = []
        if not root:
            return ans
        qu.append(root)
        while qu:
            lst = []
            n = len(qu)
            for i in range(n):
                val = qu.pop(0)
                lst.append(val.val)
                if val.left:
                    qu.append(val.left)
                if val.right:
                    qu.append(val.right)     
            ans.append(lst)
        return ans

        