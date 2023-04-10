class Solution:
    def isValid(self, s: str) -> bool:
        match = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in match: stack.append(char)
            else:
                if not stack: return False
                if match[stack[-1]] == char: stack.pop()
                else: return False
        return not stack 