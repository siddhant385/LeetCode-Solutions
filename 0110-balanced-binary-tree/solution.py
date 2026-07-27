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
        def helper(root,lvl):
            if not root:
                return lvl
            a = helper(root.left,lvl+1)
            b = helper(root.right,lvl+1)
            return max(a,b)
        return abs(helper(root.left,0) - helper(root.right,0)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
        