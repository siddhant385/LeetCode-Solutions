# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st1 = [root]
        st2 = []
        while st1:
            val = st1.pop()
            st2.append(val)
            if val.left:
                st1.append(val.left)
            if val.right:
                st1.append(val.right)
        ans = []
        while st2:
            val = st2.pop()
            ans.append(val.val)
        return ans
            


        