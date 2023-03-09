# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic, cur, pos = {}, head, 0
        while cur:
            if cur not in dic: dic[cur] = pos
            else: return cur
            pos += 1
            cur = cur.next
        return None