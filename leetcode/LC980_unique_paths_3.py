class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N, t, z = len(grid), len(grid[0]), [0], 0
        for i, j in itertools.product(range(M), range(N)):
            if grid[i][j] == 0: z += 1
            if grid[i][j] == 1: a, b = i, j
            if grid[i][j] == 2: e, f = i, j
        grid[a][b] = 0
        def dfs(i, j, c):
            if (i, j) == (e, f): t[0] += (c == z + 1)
            if grid[i][j]: return
            grid[i][j] = -1
            for x, y in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1): 0 <= x < M and 0 <= y < N and dfs(x, y, c + 1)
            grid[i][j] = 0
        dfs(a, b, 0)
        return t[0]