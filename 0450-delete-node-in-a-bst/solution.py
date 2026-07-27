# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        prev = None
        while curr and curr.val != key:
            prev = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            return root
        
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            
            if not prev: 
                return child
            
            if prev.left == curr:
                prev.left = child
            else:
                prev.right = child
                
        else:
            succ_prev = curr
            succ = curr.right
            while succ.left:
                succ_prev = succ
                succ = succ.left
            
            curr.val = succ.val
            
            if succ_prev.left == succ:
                succ_prev.left = succ.right
            else:
                succ_prev.right = succ.right
                
        return root