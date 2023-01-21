class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(i, address):
            if i == len(s):
                if len(address) == 4:
                    res.append('.'.join(map(str, address)))
                return
            if address[-1] != 0 and address[-1] * 10 + int(s[i]) <= 255:
                lastItem = address[-1]
                address[-1] = lastItem * 10 + int(s[i])
                backtrack(i + 1, address)
                address[-1] = lastItem
            if len(address) < 4:
                backtrack(i + 1, address + [int(s[i])])
        backtrack(1, [int(s[0])])
        return res