class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        res = 0     
        graph = defaultdict(list)
        for c1, c2 in roads:
            graph[c1].append(c2)
            graph[c2].append(c1)
        def dfs(node, par):
            nonlocal res
            totalPeople = 1
            for nei in graph[node]:
                if nei != par:
                    people, car = dfs(nei, node)
                    totalPeople += people
                    res += car
            cars = ceil(totalPeople / seats)
            return totalPeople, cars
        dfs(0, None)
        return res