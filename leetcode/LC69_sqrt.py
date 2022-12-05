class Solution:
    def mySqrt(self, x: int) -> int:
        big, now, small = x, max(x // 2, 1), 0
        while True:
            if now * now == x or small == now or big == now:
                return now
            else:
                if now ** 2 < x:
                    small, now = now, (now + big) // 2
                else:
                    big, now = now, (now + small) // 2
