# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        first = None
        last = None
        def helper(root):
            nonlocal prev,first,last
            if not root:
                return
            helper(root.left)
            if prev and prev.val > root.val:
                if not first:
                    first = prev
                    last = root
                else:
                    last = root
            prev = root
            helper(root.right)
        helper(root)
        first.val,last.val = last.val,first.val




            
            


        