class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, res = len(mat), 0
        for i in range(n): res += mat[i][i] + mat[i][n - i - 1]
        if n % 2 == 1: res -= mat[n // 2][n // 2]
        return res