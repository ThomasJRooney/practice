class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        counter, remaining, nxt, prev = 0, dummy.next, None, dummy
        while remaining:
            counter += 1
            if counter == k:
                temp = remaining.next
                remaining.next = None
                remaining = temp
                counter = 0
                nxt = prev.next
                prev.next = self.reverseList(nxt)
                nxt.next = remaining
                prev = nxt
                continue
            remaining = remaining.next
        if counter:
            nxt = prev.next
            prev.next = nxt
        return dummy.next

    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        