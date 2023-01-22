class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ret = 0
        n = str(n)
        sign = "+"
        for x in n:
            add = int(x)
            if sign == "-":
                add *= -1
            ret += add
            if sign == "+": 
                sign = "-" 
            else:
                sign = "+"
        return ret