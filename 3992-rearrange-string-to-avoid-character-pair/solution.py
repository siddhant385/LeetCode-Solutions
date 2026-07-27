class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        withx = ""
        withoutx = ""
        for i in s:
            if i == x:
                withx+=i
            else:
                withoutx+=i
        return withoutx+withx