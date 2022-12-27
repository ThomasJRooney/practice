class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        difference = []
        for i in range(len(rocks)): difference.append(capacity[i] - rocks[i])
        while additionalRocks > 0:
            min_index = difference.index(max(difference))
            if difference[min_index] == 0:
                return difference.count(0)
            for i in range(len(difference)):
                if difference[i] > 0 and difference[min_index] > difference[i]:
                    min_index = i
            difference[min_index] -= 1
            additionalRocks -= 1
        return difference.count(0)