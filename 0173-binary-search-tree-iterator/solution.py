# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.st = [root]
        self.visited = set()

        

    def next(self) -> int:
        while self.root.left and self.root not in self.visited:
            self.visited.add(self.root)
            self.st.append(self.root.left)
            self.root = self.root.left
        node = self.st.pop()
        if node.right:
            self.st.append(node.right)
            self.root = node.right
        return node.val

            


    def hasNext(self) -> bool:
        if self.st:
            return True
        return False
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()