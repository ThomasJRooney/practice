class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        s = set()
        for val in dic.values():
            if val in s:
                return False
            else:
                s.add(val)
        return True
