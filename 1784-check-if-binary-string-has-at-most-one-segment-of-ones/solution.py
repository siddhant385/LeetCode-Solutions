class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        prev = "1"
        for i in range(1,n):
            if s[i] != prev and s[i] =="1":
                return False
            prev = s[i]
        return True



        