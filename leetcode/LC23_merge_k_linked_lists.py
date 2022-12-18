class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergeTemp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergeTemp.append(self.mergeList(l1, l2))
            lists = mergeTemp
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next