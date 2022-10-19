class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix:
                for i in range(len(matrix) - 1):
                    if len(matrix[i]) != 0:
                        ret.append(matrix[i].pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix:
                for i in range(1, len(matrix) + 1):
                    if len(matrix[-i]) != 0:
                        ret.append(matrix[-i].pop(0))
        return ret