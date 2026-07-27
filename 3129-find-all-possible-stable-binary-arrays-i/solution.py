class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def helper(z, o, last):
            if z == 0 and o == 0:
                return 1
            if z < 0 or o < 0:
                return 0

            if (z, o, last) in memo:
                return memo[(z, o, last)]

            ans = 0

            if last == 0:  # last placed zero, now place ones
                for i in range(1, min(limit, o) + 1):
                    ans = (ans + helper(z, o - i, 1)) % MOD

            else:  # last placed one, now place zeros
                for i in range(1, min(limit, z) + 1):
                    ans = (ans + helper(z - i, o, 0)) % MOD

            memo[(z, o, last)] = ans
            return ans

        return (helper(zero, one, 0) + helper(zero, one, 1)) % MOD