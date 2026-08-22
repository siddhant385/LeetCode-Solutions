class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit = 0
        sums = 0
        product = 1
        q = n
        while n>0:
            digit = n%10
            n //= 10
            sums += digit
            product *= digit
        
        if  q%(product+sums)== 0:
            return True
        return False


        