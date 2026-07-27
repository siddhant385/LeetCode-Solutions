class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = len(num)-1
        ans = ""
        while l>=0:
            if int(num[l]) %2 != 0:
                for i in range(0,l+1):
                    if int(num[i]) != 0:
                        ans = num[i:l+1:]
                        return ans
            else:
                l -= 1
        return ans
        