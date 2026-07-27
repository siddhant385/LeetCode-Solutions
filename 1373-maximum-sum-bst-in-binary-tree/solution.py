# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = [0]
        def dfs(root):
            if not root:
                return 0, float('-inf') , float('inf') , True
            left_sum,left_max_limit,left_min_limit,left_is_bst = dfs(root.left)
            right_sum,right_max_limit,right_min_limit,right_is_bst = dfs(root.right)
            if left_is_bst and right_is_bst and left_max_limit < root.val < right_min_limit:
                c_sum = left_sum+right_sum+root.val
                max_sum[0] = max(c_sum,max_sum[0])
                return c_sum,max(right_max_limit,root.val),min(left_min_limit,root.val),True
            else:
                return 0,float('inf'),float('-inf'),False
        dfs(root)
        return max_sum[0]





            
        