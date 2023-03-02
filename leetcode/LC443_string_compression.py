class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1: return 1
        ans, i = 0, 0
        while i < n:
            letter = chars[i]
            count = 0
            while i < n and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        return ans