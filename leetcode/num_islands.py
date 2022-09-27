'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def bfs(r, c):
            stack = [(r, c)]
            neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while len(stack) > 0:
                cur_r, cur_c = stack.pop()
                visit.add((cur_r, cur_c))
                for n in neighbors:
                    rd = cur_r + n[0]
                    cd = cur_c + n[1]
                    if rd < rows and rd >= 0 and cd < cols and cd >= 0 and (rd, cd) not in visit and grid[rd][cd] == "1":
                        stack.append((rd, cd))
                
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
