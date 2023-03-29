# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            if cur.val == val and prev:
                prev.next = cur.next
                cur = cur.next
                continue
            elif cur.val == val and not prev:
                head = head.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next
        return head