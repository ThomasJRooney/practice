'''
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

 

Example 1:

Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.

'''

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        idxs_sorted_by_value = sorted(range(n), key=lambda i: A[i])
        odd_next_hops = self.get_next_hops(idxs_sorted_by_value)
        idxs_sorted_by_value.sort(key=lambda i: -A[i])
        even_next_hops = self.get_next_hops(idxs_sorted_by_value)

        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True
        for i in reversed(range(n - 1)):
            odd_next_hop, even_next_hop = odd_next_hops[i], even_next_hops[i]
            if odd_next_hop: odd[i] = even[odd_next_hop]
            if even_next_hop: even[i] = odd[even_next_hop]

        return sum(odd)

    def get_next_hops(self, idxs_sorted_by_value):
        next_hop = [None] * len(idxs_sorted_by_value)
        stack = []

        for i in idxs_sorted_by_value:
            while stack and stack[-1] < i:
                next_hop[stack.pop()] = i
            stack.append(i)

        return next_hop

