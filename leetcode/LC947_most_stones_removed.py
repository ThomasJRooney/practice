class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph_x = defaultdict(list)
        graph_y = defaultdict(list)
        for x, y in stones:
            graph_x[x].append(y)
            graph_y[y].append(x)
        def dfs(x, y):
            nonlocal visited
            if (x, y) not in visited:
                visited.add((x, y))
                for n_y in graph_x[x]:
                    dfs(x, n_y)
                for n_x in graph_y[y]:
                    dfs(n_x, y)
        connectedComponent = 0
        visited = set()
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                connectedComponent += 1
        return len(stones) - connectedComponent
