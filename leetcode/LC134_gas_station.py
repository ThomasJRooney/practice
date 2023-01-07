class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if total_surplus < 0 else start

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, total_gas, remaining = 0, 0, 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            remaining += gas[i] - cost[i]
            if remaining < 0:
                start = i + 1
                remaining = 0
        return start if total_gas >= 0 else -1
