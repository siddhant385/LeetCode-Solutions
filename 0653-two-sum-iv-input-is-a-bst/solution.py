# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        st = [root]
        while st:
            node = st.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left: st.append(node.left)
            if node.right: st.append(node.right)
        return False
            


            
        


        