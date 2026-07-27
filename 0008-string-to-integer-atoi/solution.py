class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. digits
        res = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            i += 1

        return sign * res
