# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        rstr = ""
        if not root:
            return rstr
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                root = q.popleft()
                if not root:
                    rstr += "#,"
                    continue
                else:
                    rstr+=str(root.val)+","
                q.append(root.left)
                q.append(root.right)
        return rstr
                        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data =="":return None
        data = data.split(",")
        data.pop()
        troot = TreeNode(int(data[0]))
        q = deque([troot])
        t = len(data)
        p = 1
        while q and p < t:
            left = None
            right = None
            if data[p] != "#":
                left = TreeNode(int(data[p]))
            p+=1
            if data[p] != "#":
                right = TreeNode(int(data[p]))
            p+=1
            root = q.popleft()
            if not root:
                continue
            root.left = left
            root.right = right
            if left:
                q.append(left)
            if right:
                q.append(right)
        return troot

                

            
            

            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
