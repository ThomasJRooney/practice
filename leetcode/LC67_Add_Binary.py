class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = abs(len(a) - len(b))
        a = "0" * diff * (len(a) < len(b)) + a
        b = "0" * diff * (len(b) < len(a)) + b
        n = len(a)
        res = []
        carry = 0
        for i in range(n - 1, -1, -1):
            bit1, bit2 = int(a[i]), int(b[i])
            currBit = (bit1 + bit2 + carry) % 2
            carry = (bit1 + bit2 + carry) // 2
            res.append(str(currBit))
        if carry:
            res.append(str(carry))
        return "".join(res)[::-1]

    def addBinary(self, a: str, b: str) -> str:
        dif = abs(len(a) - len(b))
        a, b = '0' * dif * (len(a) < len(b)) + a, '0' * dif * (len(b) < len(a)) + b
        n, res, carry = len(a), [], 0
        for i in range(n - 1, -1, -1):
            bit1, bit2 = int(a[i]), int(b[i])
            cur = (bit1 + bit2 + carry) % 2
            carry = (bit1 + bit2 + carry) // 2
            res.append(str(cur))
        if carry: res.append(str(carry))
        return "".join(res)[::-1]
