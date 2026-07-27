# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        n = len(inorder)
        for i in range(n):
            mp[inorder[i]] = i
        
        def helper(preStart,preEnd,inStart,inEnd):
            if preStart > preEnd or inStart > inEnd:return None
            root = TreeNode(preorder[preStart])
            root_index = mp[preorder[preStart]] 
            left_length = root_index - inStart
            root.left = helper(preStart+1,preStart+left_length,inStart,root_index-1)
            root.right = helper(preStart + left_length + 1,preEnd,root_index + 1,inEnd)
            return root
        return helper(0,n-1,0,n-1)

        