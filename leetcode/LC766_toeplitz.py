class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if row != 0 and col != 0 and matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True