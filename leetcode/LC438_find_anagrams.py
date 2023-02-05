class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        index = []
        p_sort = ''.join(sorted(p))
        for i in range(len(s) - len(p) + 1):
            tmp = s[i:i+len(p)]
            tmp = ''.join(sorted(tmp))
            if tmp == p_sort:
                index.append(i)
        return index