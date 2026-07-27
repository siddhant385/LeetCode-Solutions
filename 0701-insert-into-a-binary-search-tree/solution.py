# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val > val:
                if not curr.left:
                    break
                curr = curr.left
            else:
                if not curr.right:
                    break
                curr = curr.right
        node = TreeNode(val)
        if not curr:
            root = node
            return root
        if curr.val > val:
            curr.left = node
        else:
            curr.right = node
        return root
            
        
        