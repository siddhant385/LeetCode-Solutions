class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
            
        def helper(index, current_total):
            if index >= len(s) or not s[index].isdigit():
                return current_total
            
            # Digit ko number mein badlo
            digit = int(s[index])
            new_total = current_total * 10 + digit
            
            # Overflow check (LeetCode ki requirement)
            if sign * new_total > 2**31 - 1: return 2**31 - 1
            if sign * new_total < -2**31: return 2**31
            
            return helper(index + 1, new_total)

        return sign * helper(0, 0)