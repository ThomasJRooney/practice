class Solution(object):
    def robotSim(self, commands, obstacles):
        obstacles = set(map(tuple, obstacles))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        med = 0
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        med = max(med, x*x + y*y)
        return med
