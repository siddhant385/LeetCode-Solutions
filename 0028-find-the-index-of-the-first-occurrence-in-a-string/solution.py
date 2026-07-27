class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        arr = []
        sz = len(needle)
        for i,stra in enumerate(haystack):
            if stra == needle[0]:
                arr.append(i)
        for i in arr:
            if needle == haystack[i:i+sz]:
                return i

        


                

        