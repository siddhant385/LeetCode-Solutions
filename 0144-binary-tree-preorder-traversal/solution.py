# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(ans,root):
            if root == None:
                return []
            ans.append(root.val)
            if root.left:
                helper(ans,root.left)
            if root.right:
                helper(ans,root.right)
            return ans
        return helper(ans,root)

        