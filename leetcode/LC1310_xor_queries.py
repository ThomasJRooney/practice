class Solution(object):
    def xorQueries(self, arr, queries):
        if not arr or not queries:
            return []
        
        qset = [list(item) for item in set(tuple(sublist) for sublist in queries)]

        qdic = {}
        for left, right in qset:
            seq = arr[left:right+1]
            app = seq[0]
            for i in range(1, len(seq)):
                app ^= seq[i]
            qdic[(left, right)] = app

        ret = []
        for l, r in queries:
            ret.append(qdic[(l, r)])
        return ret
