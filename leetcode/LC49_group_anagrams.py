class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        dic = {}
        for s in strs:
            test = ''.join(sorted(s))
            if test in dic:
                ret[dic[test]].append(s)
            else:
                dic[test] = len(ret)
                ret.append([s])
        return ret