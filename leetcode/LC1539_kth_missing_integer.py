class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range(1, arr[0]): 
            missing.append(i)
            if len(missing) == k: return missing[k - 1]

        for i in range(arr[0], arr[-1]):
            if i not in arr:
                missing.append(i)
                if len(missing) == k: return missing[k - 1]
        cur = arr[-1] + 1
        while len(missing) < k:
            missing.append(cur)
            cur += 1
        return missing[k - 1]