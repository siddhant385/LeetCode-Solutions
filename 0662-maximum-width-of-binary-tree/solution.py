# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root,1]])
        ans = 0
        while q:
            n = len(q)
            lb = float('inf')
            rb = 0
            for i in range(n):
                node,num = q.popleft()
                rb = num
                lb = min(lb,rb)
                if node.left:
                    q.append([node.left,2*num])
                if node.right:
                    q.append([node.right,2*num+1])
            ans = max(ans,rb-lb+1)
        return ans


        