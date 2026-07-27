class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        mul = 0
        for letter in range(len(columnTitle)-1,-1,-1):
            for i,char in enumerate(alpha):
                if columnTitle[letter] == char:
                    ans += (i+1) * pow(26,mul)
            mul +=1
        return ans
                    



        