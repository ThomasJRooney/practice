class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [set() for _ in range(n)]
        for s, e in edges:
            g[s].add(e)
            g[e].add(s)
        visited = [False] * n
        self.dfs(g, visited, source)
        return visited[destination]
    
    def dfs(self, g, visited, v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                self.dfs(g, visited, to)