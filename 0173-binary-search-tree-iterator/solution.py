# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.st = []
        self.go_to_left(self.root)


    def next(self) -> int:
        node = self.st.pop()
        if node.right:
            self.go_to_left(node.right)
        return node.val

    def go_to_left(self,curr):
        while curr:
            self.st.append(curr)
            curr =curr.left
        


    def hasNext(self) -> bool:
        if self.st:
            return True
        return False
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()