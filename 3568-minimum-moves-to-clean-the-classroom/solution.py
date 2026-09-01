class Solution:

  def minMoves(self, classroom: List[str], energy: int) -> int:
    q = deque()
    # visited dictionary: (row, col, mask) -> min_energy
    visited = {}
    total_litter = 0
    m = len(classroom)
    n = len(classroom[0])
    l = {}
    init = 0

    for i in range(m):
      for j in range(n):
        if classroom[i][j] == 'S':
          visited[(i, j, 0)] = 0
          q.append((i, j, 0, 0, 0))
        elif classroom[i][j] == 'L':
          l[i, j] = init
          init += 1
          total_litter += 1

    target_mask = (1 << total_litter) - 1

    while q:
      row, col, mask, start_energy, moves = q.popleft()

      if mask == target_mask:
        return moves

      if start_energy >= energy:
        continue

      drow = [1, 0, -1, 0]
      dcol = [0, -1, 0, 1]

      for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]

        if 0 <= nrow < m and 0 <= ncol < n and classroom[nrow][ncol] != 'X':
          new_mask = mask
          if classroom[nrow][ncol] == 'L':
            new_mask |= 1 << l[(nrow, ncol)]

          new_energy = start_energy + 1
          if classroom[nrow][ncol] == 'R':
            new_energy = 0 

          state = (nrow, ncol, new_mask)
          if state not in visited or new_energy < visited[state]:
            visited[state] = new_energy
            q.append((nrow, ncol, new_mask, new_energy, moves + 1))

    return -1