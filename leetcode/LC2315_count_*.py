class Solution:
    def countAsterisks(self, s: str) -> int:
        count, inPair = 0, False
        for i in range(len(s)):
            if not inPair and s[i] == "|": inPair = True
            elif inPair and s[i] == "|": inPair = False
            elif not inPair and s[i] == "*": count += 1
        return count