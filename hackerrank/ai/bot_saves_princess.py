#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    r, c = len(grid) - 1, len(grid[0]) - 1
    cur_r, cur_c = len(grid) // 2, len(grid[0]) // 2
    p_r, p_c = None, None
    if grid[0][0] == 'p': p_r, p_c = 0, 0
    elif grid[0][c] == 'p': p_r, p_c = 0, c
    elif grid[r][0] == 'p': p_r, p_c = r, 0
    elif grid[r][c] == 'p': p_r, p_c = r, c
    ret = ""
    while cur_r != p_r or cur_c != p_c:
        if p_r < cur_r:
            cur_r -= 1
            ret += "UP\n"
        elif p_r > cur_r:
            cur_r += 1
            ret += "DOWN\n"
        if p_c < cur_c:
            cur_c -= 1
            ret += "LEFT\n"
        elif p_c > cur_c:
            cur_c += 1
            ret += "RIGHT\n"
    print(ret)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)