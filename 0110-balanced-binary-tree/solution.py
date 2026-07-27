# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag = True
        def helper(root,lvl):
            nonlocal flag
            if not root:
                return lvl
            a = helper(root.left,lvl+1)
            b = helper(root.right,lvl+1)
            if abs(a-b) > 1:
                flag = False
            return max(a,b)
        helper(root,0)
        return flag
            
        