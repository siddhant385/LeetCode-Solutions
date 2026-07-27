# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        mp = {}
        for n,i in enumerate(inorder):
            mp[i] = n
        n = len(preorder)
        def helper(preStart,preEnd,inStart,inEnd):
            if preStart > preEnd or inStart > inEnd:
                return
            root = TreeNode(preorder[preStart])
            root_value = mp[root.val]
            left_length = root_value - inStart
            root.left = helper(preStart+1,preStart+left_length,inStart,root_value-1)
            root.right = helper(preStart+left_length+1,preEnd,root_value+1,inEnd)
            return root
        return helper(0,n-1,0,n-1)

        