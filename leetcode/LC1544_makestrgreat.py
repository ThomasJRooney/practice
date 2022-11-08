class Solution:
    def makeGood(self, s: str) -> str:
        def good(s):
            for i in range(len(s) - 1):
                if (s[i].isupper() and s[i + 1].islower() and s[i].lower() == s[i + 1]) or (s[i].islower() and s[i + 1].isupper() and s[i] == s[i + 1].lower()):
                    s = s[:i] + s[i+2:]
                    return good(s)
            return s
        return good(s)
        
