class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        lst = list(text)
        ans = 0
        while True:
            for i in "balloon":
                if i not in lst:
                    a = False
                    return ans
                lst.remove(i)
            ans +=1
        return ans
            