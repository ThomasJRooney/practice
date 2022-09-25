'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # loop through each cell check if there is a path to the p and a
        # if both add to answer
        
        ans = []
        rows, cols = len(heights), len(heights[0])
        
        def search(r, c):
            atlantic = False
            pacific = False
            stack = [(r, c)]
            neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            visit = set()
            while len(stack) > 0:
                if atlantic and pacific:
                    return True
                cur_r, cur_c = stack.pop()
                visit.add((cur_r, cur_c))
                cur_val = heights[cur_r][cur_c]
                # pacific up and left
                if not pacific:
                    if cur_r == 0 or cur_c == 0
                        pacific = True
                
                # atlantic down and right
                if not atlantic:
                    if cur_r == rows - 1:
                        atlantic = True
                    if cur_c == cols - 1:
                        atlatic = True
                
                for n in neighbors:
                    n_row = cur_r + n[0]
                    n_col = cur_c + n[1]
                    if n_row > 0 and n_row < rows and n_col > 0 and n_col < cols:
                        n_val = heights[n_row][n_col]

                        if n_val <= cur_val and (n_row, n_col) not in visit:
                            stack.append((n_row, n_col))
                            
            if atlantic and pacific:
                return True
            return False
                
        
        
        for row in range(rows):
            for col in range(cols):
                if search(row, col):
                    ans.append([row, col])
        return ans
