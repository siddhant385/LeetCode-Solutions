# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = [0]
        def helper(upper_bound):
            if i[0] >= len(preorder) or preorder[i[0]] > upper_bound:
                return 
            root = TreeNode(preorder[i[0]])
            i[0] +=1
            root.left = helper(root.val)
            root.right = helper(upper_bound)
            return root
        return helper(float('inf'))



        