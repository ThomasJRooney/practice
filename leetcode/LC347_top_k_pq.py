class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap, res = [], []
        for num, freq in counter.items(): heapq.heappush(heap, (-freq, num))
        for i in range(k): res.append(heapq.heappop(heap)[1])
        return res