class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            count, total_weight = 1, 0
            for weight in weights:
                total_weight += weight
                if total_weight > mid:
                    count += 1
                    total_weight = weight
            if count > days: left = mid + 1
            else: right = mid
        return left