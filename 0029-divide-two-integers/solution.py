class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        ans = 0
        a,b = abs(dividend), abs(divisor)
        sign = 1
        if (dividend < 0 and divisor >0) or (dividend >0 and divisor <0):
            sign = -1
        else:
            sign = 1
        if a == b:
            return sign * 1
        while a >= b:
            cnt = 0
            while a >= b << (cnt+1):
                cnt +=1
            a -= b<<(cnt)
            ans += 1<< cnt
        if sign*ans >INT_MAX:
            return INT_MAX
        if sign*ans < INT_MIN:
            return INT_MIN
        return sign*ans
        
        
        