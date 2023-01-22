class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if "1" in s and "1" in target and "0" in s and "0" in target:
            return True
        if "1" in target and "1" in s:
            return True
        if s == target:
            return True
        return False