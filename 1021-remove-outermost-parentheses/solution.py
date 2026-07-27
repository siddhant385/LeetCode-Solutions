class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = -1
        res = ""
        for i in range(len(s)):
            if s[i] == "(": 
                depth+=1
            else:
                depth -=1
            if depth >=1 and s[i] =="(" or depth >=0 and s[i] ==")":
                res+=s[i]
            
        return res
            



                



        