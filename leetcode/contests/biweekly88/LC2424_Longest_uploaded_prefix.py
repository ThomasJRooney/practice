class LUPrefix:

    def __init__(self, n: int):
        self.n = n + 1
        self.uploaded = [0] * self.n
        self.long = 0

    def upload(self, video: int) -> None:
        self.uploaded[video - 1] = 1
        c = self.long
        for i in range(self.long, self.n):
            if self.uploaded[i] == 1:
                c += 1
            else:
                self.long = c
                return

    def longest(self) -> int:
        return(self.long)

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()