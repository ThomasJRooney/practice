class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split()
        if len(s) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in dic.keys() and s[i] in dic.values():
                return False
            elif pattern[i] not in dic.keys() and s[i] not in dic.values():
                dic[pattern[i]] = s[i]
            if pattern[i] in dic.keys():
                if dic[pattern[i]] != s[i]:
                    return False
        return True