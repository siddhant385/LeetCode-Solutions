class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        num = n
        sqr = 0
        digitSum = 0
        while num > 0:
            dig = num % 10
            num = num // 10
            sqr += dig*dig
            digitSum += dig
        if sqr - digitSum >= 50:
            return True
        else:
            return False
            
            
        