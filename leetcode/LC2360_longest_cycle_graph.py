class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        long, step, node_times = -1, 1, [0] * len(edges)
        for cur in range(len(edges)):
            if node_times[cur] > 0: continue
            start = step
            u = cur
            while u != -1 and node_times[u] == 0:
                node_times[u] = step
                step += 1
                u = edges[u]
            if u != -1 and node_times[u] >= start: long = max(long, step - node_times[u])
        return long