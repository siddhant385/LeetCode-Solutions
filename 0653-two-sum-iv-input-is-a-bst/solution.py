# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []
        def helper(root):
            if not root:
                return
            left = helper(root.left)
            inorder.append(root.val)
            right = helper(root.right)
        helper(root)
        l = 0
        r = len(inorder)-1
        while l < r:
            sums = inorder[l] + inorder[r]
            if sums > k:
                r-=1
            elif sums == k:
                return True
            else:
                l+=1
        return False



        