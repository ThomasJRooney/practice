from collections import defaultdict

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        def one_land(grid):
            for x, row in enumerate(grid):
                for y, val in enumerate(row):
                    if val: return (x, y)
        x, y = one_land(grid)
        q = [(x, y)]
        first_land = [(x, y)]
        visit = defaultdict(lambda:False, {})
        visit[(x, y)] = True
        while first_land:
            x, y = first_land.pop(0)
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx in range(n) and ny in range(m):
                    if grid[nx][ny]:
                        if not visit[(nx, ny)]:
                            first_land.append((nx, ny))
                            q.append((nx, ny))
                            visit[(nx, ny)] = True
        cost = 0
        while q:
            for i in range(len(q)):
                x, y = q.pop(0)
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx in range(n) and ny in range(m):
                        if not visit[(nx, ny)]:
                            if grid[nx][ny]: return cost
                            else: 
                                q.append((nx, ny))
                                visit[(nx, ny)] = True
            cost += 1
        return None