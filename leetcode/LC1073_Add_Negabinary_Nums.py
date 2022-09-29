class Solution(object):
    def addNegabinary(self, arr1, arr2):
        # sum -> res, carry
        lookup = { -1: (1, 1), 0: (0, 0), 1: (1, 0), 2: (0, -1), 3: (1, -1) }
        carry = 0
        ret = []

        while len(arr1) > 0 or len(arr2) > 0:
            b1 = 0
            if len(arr1) > 0:
                b1 = arr1.pop()
            b2 = 0
            if len(arr2) > 0:
                b2 = arr2.pop()
            idx = b1 + b2 + carry
            res, carry = lookup[idx]
            ret.append(res)

        while carry != 0:
            res, carry = lookup[carry]
            ret.append(res)

        while len(ret) > 1 and ret[-1] == 0:
            ret.pop()
        return ret[::-1]
