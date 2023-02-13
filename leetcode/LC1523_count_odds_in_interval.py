class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 1: high += 1
        return math.ceil((high - low) / 2)