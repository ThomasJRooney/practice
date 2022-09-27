class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # add every 10 char substring to a map
        # if that substring is already in map we know it occured twice
        if len(s) < 10:
            return []
        freqMap = {}
        ret = []
        l = 0
        r = 10
        while r <= len(s):
            ss = s[l:r]
            if ss in freqMap:
                freqMap[ss] += 1
                if freqMap[ss] == 2:
                    ret.append(ss)
            else:
                freqMap[ss] = 1
            l += 1
            r += 1
        
        return ret
