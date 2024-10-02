class Solution(object):
    def arrayRankTransform(self, arr):
        out = [] 
        if not arr:
            return out
        sortarr = sorted(list(set(arr)))
        dic = {}
        for i in range(len(sortarr)):
            dic[sortarr[i]] = i + 1
        for elem in arr:
            out.append(dic[elem])
        return out
