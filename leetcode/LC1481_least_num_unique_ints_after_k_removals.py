class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        counter = {}
        for n in arr:
            counter[n] = counter.get(n, 0) + 1
        elements = sorted(counter.items(), key=lambda x: x[1])

        for key, value in elements:
            if value <= k:
                k -= value
                del counter[key]
            else:
                break
        return len(counter)
