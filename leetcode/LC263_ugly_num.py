# recursive solution
class Solution:
    def isUgly(self, n: int) -> bool:
        nums = [1, 2, 3, 5]
        if n in nums:
            return True
        elif n == 0:
            return False
        elif n % 2 == 0:
            return self.isUgly(n / 2)
        elif n % 3 == 0:
            return self.isUgly(n / 3)
        elif n % 5 == 0:
            return self.isUgly(n / 5)
        else:
            return False
