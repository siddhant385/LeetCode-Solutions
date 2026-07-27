# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        curr = root
        while curr != None:
            if curr.left == None:
                ans.append(curr.val)
                curr = curr.right
            else:
                left = curr.left
                while left.right != None and left.right !=curr:
                    left = left.right
                if left.right == None:
                    left.right = curr
                    curr = curr.left
                else:
                    left.right = None
                    ans.append(curr.val)
                    curr = curr.right
        return ans