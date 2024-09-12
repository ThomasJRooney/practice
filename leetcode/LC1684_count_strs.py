class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allow = set(allowed)
        ret = 0
        for word in words:
            if all(char in allow for char in word):
                ret += 1
        return ret
