class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Initiating variables
        same_color = image[sr][sc]
        image[sr][sc] = color
        m = len(image)
        n = len(image[0])
        q = deque([(sr,sc)])
        visited = set((sr,sc))
        d_row = [1,0,-1,0]
        d_col = [0,1,0,-1]
        while q:
            r,c = q.popleft()
            for i in range(4):
                row = r+d_row[i]
                col = c+d_col[i]
                if 0 <= row < m and 0 <= col < n and (row,col) not in visited and image[row][col] == same_color:
                    q.append((row,col))
                    image[row][col] = color
                    visited.add((row,col))
        return image
                


        