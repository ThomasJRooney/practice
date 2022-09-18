class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs, cs, box = {}, {}, {}
        rows, cols = 9, 9
        for row in range(rows):
            rs[row] = []
            for col in range(cols):
                if col not in cs:
                        cs[col] = []
                
                if board[row][col] != ".":
                    if board[row][col] not in rs[row]:
                        rs[row].append(board[row][col])
                    else:
                        return False
                    
                    if board[row][col] not in cs[col]:
                        cs[col].append(board[row][col])
                    else:
                        return False 
                    
                    br = row // 3
                    bc = col // 3
                    shorthand = str(br) + str(bc)

                    if shorthand not in box:
                        box[shorthand] = []
                    
                    if board[row][col] not in box[shorthand]:
                        box[shorthand].append(board[row][col])
                    else:
                        return False
        return True
