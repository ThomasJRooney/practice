class Solution:
    def isFascinating(self, n: int) -> bool:
        model = "123456789"
        concat = str(n) + str(n * 2) + str(n * 3)
        concat = [int(concat[i]) for i in range(len(concat))]
        concat.sort()
        concat = [str(i) for i in concat]
        concat = "".join(concat)
        if model == concat: return True
        return False