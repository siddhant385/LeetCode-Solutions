class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0       # total length of valid subsequence
        value = 0       # binary value of the subsequence so far
        power = 0       # bit position from right

        # Traverse from right (LSB) to left
        for i in range(len(s) - 1, -1, -1):
            bit = s[i]
            if bit == '0':
                count += 1  # always include 0
            else:
                if power < 32 and value + (1 << power) <= k:
                    value += (1 << power)
                    count += 1
                else:
                    # Can't include this '1', as it would exceed k
                    pass
            if bit == '1' or bit == '0':
                power += 1

        return count

            