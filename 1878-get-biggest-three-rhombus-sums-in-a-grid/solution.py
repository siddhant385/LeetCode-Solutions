class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        s = set()

        for i in range(m):
            for j in range(n):

                # area = 0 rhombus
                s.add(grid[i][j])

                k = 1
                while True:
                    if (i-k < 0 or i+k >= m or j-k < 0 or j+k >= n):
                        break

                    total = 0

                    # top -> right
                    x, y = i-k, j
                    for d in range(k):
                        total += grid[x+d][y+d]

                    # right -> bottom
                    x, y = i, j+k
                    for d in range(k):
                        total += grid[x+d][y-d]

                    # bottom -> left
                    x, y = i+k, j
                    for d in range(k):
                        total += grid[x-d][y-d]

                    # left -> top
                    x, y = i, j-k
                    for d in range(k):
                        total += grid[x-d][y+d]

                    s.add(total)
                    k += 1

        ans = sorted(s, reverse=True)
        return ans[:3]