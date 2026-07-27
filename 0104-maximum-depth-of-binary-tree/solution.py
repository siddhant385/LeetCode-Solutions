# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root,lvl):
            if not root:
                return lvl
            lvl +=1
            a = helper(root.left,lvl)
            b = helper(root.right,lvl)
            return max(a,b)
        return helper(root,0)
            
        
        

        