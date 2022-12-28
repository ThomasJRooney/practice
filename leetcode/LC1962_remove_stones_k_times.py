import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        while k > 0:
            index, remove = 0, 0
            for i in range(len(piles)):
                if math.floor(piles[i] / 2) > remove:
                    index, remove = i, math.floor(piles[i] / 2)
            piles[index] -= remove
            k -= 1
        return sum(piles)

import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:   
        heap = [-num for num in piles]
        heapq.heapify(heap)
        for _ in range(k):
            cur = -heapq.heappop(heap)
            remove = cur // 2
            heapq.heappush(heap, -(cur - remove))
        return -sum(heap)