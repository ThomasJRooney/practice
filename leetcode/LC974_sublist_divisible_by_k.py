class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_freq = defaultdict(int)
        rem_freq[0] = 1
        res = prefixSum = 0
        for n in nums:
            prefixSum += n
            remainder = prefixSum % k
            res += rem_freq[remainder]
            rem_freq[remainder] += 1
        return res