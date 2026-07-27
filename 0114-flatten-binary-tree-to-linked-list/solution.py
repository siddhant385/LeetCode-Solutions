# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # Ek global/class-level pointer jo hamesha already processed list ke head par point karega
        self.prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # 1. Sabse pehle poore Right Subtree ko process karo
        self.flatten(root.right)
        
        # 2. Phir poore Left Subtree ko process karo
        self.flatten(root.left)
        
        # 3. Ab Root par aakar pointers adjust karo
        root.right = self.prev
        root.left = None
        
        # Current node ab agle (upar wale) node ke liye 'prev' ban jayega
        self.prev = root