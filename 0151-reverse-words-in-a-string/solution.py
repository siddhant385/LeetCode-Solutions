class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = ""
        for word in words:
            if word != "":
                res+= " "+word[-1::-1]
        res = res[1::]
        return res[-1::-1]

        