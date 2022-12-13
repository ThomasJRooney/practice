class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        if len(matrix) == 1: return matrix[0][0]
        length = len(matrix)
        for i in range(1, length):
            for j in range(0, length):
                if j == 0:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j == length - 1:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j])
                else:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])
        return min(matrix[-1])
        