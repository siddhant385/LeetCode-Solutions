class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "([{":
                l.append(i)
            else:
                if l and self.left(i) == l[-1]:
                    l.pop()
                else:
                    return False
        if l==[]:
            return True
        else:
            return False
    def left(self,sym):
        if sym == ")": return "("
        if sym == "]": return "["
        else: return "{"
        