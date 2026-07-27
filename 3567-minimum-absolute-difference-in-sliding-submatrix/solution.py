from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                values = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.add(grid[x][y])

                if len(values) <= 1:
                    row.append(0)
                    continue

                sorted_vals = sorted(values)
                min_diff = float('inf')

                for t in range(1, len(sorted_vals)):
                    min_diff = min(min_diff, sorted_vals[t] - sorted_vals[t - 1])

                row.append(min_diff)

            ans.append(row)

        return ans