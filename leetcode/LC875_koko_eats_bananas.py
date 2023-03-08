class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def can_eat_all_bananas(speed):
            time = 0
            for pile in piles: time += (pile + speed - 1) // speed
            return time <= h
        while left < right:
            mid = (left + right) // 2
            if can_eat_all_bananas(mid): right = mid
            else: left = mid + 1
        return left