class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 < 101:
            return 0
        ans = 0
        for i in range(num1,num2+1):
            digits = []
            while i != 0:
                digits.append(i % 10)
                i = i // 10
            l = 0
            r = 2
            n = len(digits)
            # print(digits)
            while r < n:
                if digits[l] > digits[l+1] and digits[r] > digits[l+1]:
                    ans += 1
                if digits[l] < digits[l+1] and digits[r] < digits[l+1]:
                    ans += 1

                l += 1
                r += 1
        return ans

            

        