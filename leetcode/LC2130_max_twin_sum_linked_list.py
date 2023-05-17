# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast, ret = head, head, 0
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        nex, prev = None, None
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex
        while prev:
            ret = max(ret, head.val + prev.val)
            prev = prev.next
            head = head.next
        return ret