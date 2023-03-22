class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads: graph[u][v] = graph[v][u] = w
        min_score, visit, q = float('inf'), set(), deque([1])
        while q:
            node = q.popleft()
            for adj, score in graph[node].items():
                if adj not in visit:
                    q.append(adj)
                    visit.add(adj)
                min_score = min(min_score, score)
        return min_score