# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        curr = root
        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                val = st.pop()
                ans.append(val.val)
                curr = val.right
        return ans

            
            

                

                
        