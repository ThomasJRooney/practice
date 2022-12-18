class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [-1 for _ in range(71)]
        answer = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            j = [x for x in arr[t - 30 + 1:] if x > -1]
            answer[i] = 0 if len(j) == 0 else min(j) - i
            arr[t - 30] = i
        return answer