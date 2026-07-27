# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        n = len(inorder)
        for i in range(n):
            mp[inorder[i]] = i
        def helper(pStart,pEnd,inStart,inEnd):
            if pStart < pEnd or inEnd < inStart:
                return None
            root = TreeNode(postorder[pStart])
            root_index = mp[root.val]
            right_length = inEnd - root_index
            root.left = helper(pStart-right_length-1,pEnd,inStart,root_index-1)
            root.right = helper(pStart-1,pStart-right_length,root_index+1,inEnd)
            return root
        return helper(n-1,0,0,n-1)

        