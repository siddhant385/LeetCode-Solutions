# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        st = [root]
        while st!=[]:
            val = st.pop()
            ans.append(val.val)
            if val.right:
                st.append(val.right)
            if val.left:
                st.append(val.left)
        return ans


        

        