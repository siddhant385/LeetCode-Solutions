class Solution:
    def checkValidString(self, s: str) -> bool:
        minv = 0
        maxv = 0
        for i in s:
            if i == "(":
                minv+= 1
                maxv +=1
            elif i == ")":
                minv = max(0,minv -1)
                maxv -=1
            else:
                minv = max(0,minv -1)
                maxv +=1
            if maxv <0:
                return False
        if minv ==0:
            return True
        return False
        