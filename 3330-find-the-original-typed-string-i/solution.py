class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = []
        i = 0
        n = len(word)

        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)  # Length of this group
            i = j

        result = 1  # The original string
        for group_len in groups:
            if group_len > 1:
                result += (group_len - 1)  # Possible shortenings

        return result
