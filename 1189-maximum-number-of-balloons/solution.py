class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        lst = list(text)
        a = True
        ans = 0
        while a:
            for i in "balloon":
                if i not in lst:
                    a = False
                    break
                lst.remove(i)
            if a == False:
                break
            ans +=1
        return ans
            