class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        graph = [set() for i in range(n)]
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        visit = [0] * n
        def dfs(node):
            if visit[node]: return 0
            visit[node] = 1
            for n in graph[node]: dfs(n)
            return 1
        return sum(dfs(node) for node in range(n)) - 1