# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-1000]
        def helper(root):
            if not root:
                return 0
            left_sum = max(0,helper(root.left))
            right_sum = max(0,helper(root.right))
            max_sum[0] =  max(max_sum[0],left_sum+right_sum+root.val)
            return max(left_sum,right_sum) + root.val
        helper(root)
        return max_sum[0]
        