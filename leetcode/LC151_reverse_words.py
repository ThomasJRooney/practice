class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([ch for ch in reversed(s.split()) if ch])