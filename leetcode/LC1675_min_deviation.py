class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        for num in nums:
            if num % 2 == 0: num = -num
            else: num = -num * 2
            heapq.heappush(max_heap, num)
        min_dev = float('inf')
        min_val = -max(max_heap)
        while len(nums) == len(max_heap):
            cur = -heapq.heappop(max_heap)
            min_dev = min(min_dev, cur - min_val)
            if cur % 2 == 0:
                min_val = min(min_val, cur // 2)
                heapq.heappush(max_heap, -cur // 2)
            else: break
        return min_dev