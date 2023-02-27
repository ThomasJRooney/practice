class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        count = 0
        for num in nums:
            if num - diff in seen and num - diff * 2 in seen: count += 1
            seen.add(num)
        return count