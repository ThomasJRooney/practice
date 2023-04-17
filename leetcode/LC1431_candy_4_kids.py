class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        if not candies : return out
        for i in range(len(candies)): out.append(True) if candies[i] + extraCandies >= max(candies) else out.append(False)
        return out