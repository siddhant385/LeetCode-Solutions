# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mp = {}
        def helper(root):
            if not root:
                return None
            if root.left:
                mp[root.left]= root
                helper(root.left)
            if root.right:
                mp[root.right] = root
                helper(root.right)
        helper(root)
        q = deque([target])
        visited = set()
        visited.add(target)
        obj = 0
        while q:
            n = len(q)
            if obj ==k:
                return [ans.val for ans in q]
            for i in range(n):
                node = q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                parent = mp.get(node,None)
                if parent and parent not in visited:
                    q.append(parent)
                    visited.add(parent)
            obj +=1
        return []

