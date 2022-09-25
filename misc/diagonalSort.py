'''
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # left to right find smallest value to swap with in diagonal and swap it
        # continue until we do the whole matrix
        rows, cols = len(mat), len(mat[0])
        
        for r in range(rows):
            for c in range(cols):
                # current number we are looking at
                cur = mat[r][c]
                min_row, min_col = r, c
                d_row, d_col = r, c
                
                # find min row, col to swap with
                while d_row + 1 < rows and d_col + 1 < cols:
                    d_row += 1
                    d_col += 1
                    if mat[d_row][d_col] < mat[min_row][min_col]:
                        min_row, min_col = d_row, d_col
                       
                # if there is a smaller number than is there swap the values
                if min_row != r and min_col != c:
                    temp = mat[min_row][min_col]
                    mat[min_row][min_col] = cur
                    mat[r][c] = temp
        return mat
    
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()
        return mat
                
