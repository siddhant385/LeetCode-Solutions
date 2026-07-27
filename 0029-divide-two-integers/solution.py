class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dvd = abs(dividend)
        dvs = abs(divisor)
        quotient = 0
        while dvd >= dvs:
            temp_divisor = dvs
            multiple = 1 

            while dvd >= (temp_divisor << 1): 
                temp_divisor <<= 1
                multiple <<= 1 
            dvd -= temp_divisor
            quotient += multiple

        result = sign * quotient

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
        