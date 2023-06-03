class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        num, i, sign = 0, 0, 1
        if s[i] == "+": i += 1
        elif s[i] == "-":
            i += 1
            sign = -1
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        num = max(min(num, 2**31 - 1), -2**31)
        return num