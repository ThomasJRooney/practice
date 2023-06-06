class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = [str(digit) for digit in digits]
        num = "".join(num)
        num = int(num) + 1
        num = str(num)
        num = [num[i] for i in range(len(num))]
        num = [int(n) for n in num]
        return num