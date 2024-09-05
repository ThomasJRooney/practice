class Solution(object):
    def missingRolls(self, rolls, mean, n):
        arr_sum = (mean * (len(rolls) + n)) - sum(rolls)
        if arr_sum < n or arr_sum > 6*n: return []
        res = [arr_sum // n] * n
        rem = arr_sum % n
        for i in range(rem): res[i] += 1
        return res
