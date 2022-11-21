class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visit = set()
        count = 0
        q = [entrance]
        nei = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            for i in range(len(q)):
                cur_r, cur_c = q.pop()
                visit.add((cur_r, cur_c))
                if [cur_r, cur_c] != entrance and (cur_r == 0 or cur_r == len(maze) - 1 or cur_c == 0 or cur_c == len(maze[0]) - 1):
                    return count
                for r, c in nei:
                    n_r, n_c = cur_r + r, cur_c + c
                    if (n_r, n_c) not in visit and n_r > -1 and n_r < len(maze) and n_c > -1 and n_c < len(maze[0]) and maze[n_r][n_c] != '+':
                        q.insert(0, [n_r, n_c])

            count += 1
        return -1
