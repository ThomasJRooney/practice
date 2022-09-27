"""
We would like to implement a simple 2 dimensional sandbox construction game. The building area is a 10 x 10 grid and each cell can be either empty, 
filled with a regular block, or a ground block which is a special type of block we will use later. We will incrementally add new functionalities to this game.

PrintBoard:
Implement a representation of the board then implement a function PrintBoard() that prints it. 
Use “. “ for empty cells, “X ” for ground blocks and “O “ for regular blocks. You can assume all the cells are initially empty.


GetNeighbors:
Implement a helper function GetNeighbors(x, y) that given the coordinates of a cell, it returns all the FILLED cells neighboring it.
Two cells are neighbors if they share a side with each other.
You can assume that x and y are coordinates within the bounds of the board.

AddBlock:
Implement a function bool AddBlock(x, y, isGround) where x and y denote the coordinates of a cell we want to fill with a block and
isGround denotes whether we want the block to be a ground block. This function should return true if the block was successfully placed and false otherwise.
You can assume x and y are valid coordinates within the board of an empty cell however
you must check that for regular(non-ground) blocks, the given coordinates are neighboring an existing block and if that’s not the case return false.

for example if top left is (0, 0) then:
AddBlock(0, 0, True):
X . . . 
. . . . 
. . . . 
. . . . 

AddBlock(0, 1, False):
X . . . 
O . . . 
. . . . 
. . . . 

AddBlock(3, 3, False):
X . . . 
O . . . 
. . . . 
. . . . 


RemoveBlock:
Implement a function RemoveBlock(x, y) where x and y denote the coordinates of a block we want to remove from the board.
Upon removal of the block at the given coordinates, some other block or groups of blocks (blocks attached to each other) might become floating so
we would like to remove those blocks as well. A block is considered floating if it’s not attached to a ground block directly or indirectly.
You can assume x and y are valid coordinates on the board of an existing non-ground block.

for example if the board currently looks like this:
X O O . 
. . O . 
. . O . 
. . . . 

then calling RemoveBlock(2, 0) should result in:
X O . . 
. . . . 
. . . . 
. . . . 

"""

class ConstructionGame:
    def __init__(self):
        self.grid = []
        for i in range(10):
            self.grid.append(['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
        
    def PrintBoard(self):
        for row in self.grid:
            colStr = ""
            for col in row:
                colStr += col + " "
            print(colStr)
    
    def GetNeighbors(self, x, y):
        neighbors = []
        possible_neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r, c in possible_neighbors:
            if x + r >= 0 and x + r < 10 and y + c >= 0 and y + c < 10 and self.grid[x + r][y + c] != '.':
                neighbors.append([x + r, y + c])
        return neighbors

    def AddBlock(self, x, y, isGround):
        if isGround:
            self.grid[x][y] = 'X'
            return True
        else:
            neighbors = self.GetNeighbors(x, y)
            if neighbors != []:
                self.grid[x][y] = 'O'
                return True 
        return False
    
    def RemoveBlock(self, x, y):
        self.grid[x][y] = '.'
        
        neighbors = self.GetNeighbors(x, y)
        
        for r, c in neighbors:
            visit = set()
            q = [[r, c]]
            shouldDeleteVisit = False
            while q:
                cur_r, cur_c = q.pop(0)
                visit.add((cur_r, cur_c))
                if self.grid[cur_r][cur_c] == 'X':
                    q = []
                elif self.grid[cur_r][cur_c] == 'O':
                    # push neighbors onto q
                    new_neighbors = self.GetNeighbors(cur_r, cur_c)
                    to_push = []
                    for nr, nc in new_neighbors:
                        if (nr, nc) not in visit:
                            to_push.append([nr, nc])
                            q.append([nr, nc])
                    if not to_push:
                        shouldDeleteVisit = True
                            
            if shouldDeleteVisit:
                for row, col in visit:
                    self.grid[row][col] = '.'
                            
        
game = ConstructionGame()
#game.PrintBoard()
game.AddBlock(0, 0, True)
game.AddBlock(0, 1, False)
game.AddBlock(0, 2, False)
game.AddBlock(0, 3, False)
game.AddBlock(0, 4, False)
game.AddBlock(0, 5, False)
game.AddBlock(0, 6, False)
game.AddBlock(0, 7, False)
game.AddBlock(0, 8, False)
game.AddBlock(0, 9, False)
game.AddBlock(1, 9, False)
game.AddBlock(2, 9, False)
game.AddBlock(3, 9, False)
game.AddBlock(4, 9, False)
game.AddBlock(5, 9, False)
game.AddBlock(3, 3, False)
game.PrintBoard()
game.RemoveBlock(0, 5)
print()
game.PrintBoard()
