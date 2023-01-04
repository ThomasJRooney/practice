class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        return (frequency := Counter(tasks)) and sum(ceil(freq / 3) for freq in frequency.values()) if (frequency := Counter(tasks)) and (1 not in frequency.values()) else -1