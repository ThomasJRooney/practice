# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds, evens = ListNode(0), ListNode(0)
        oddsHead, evensHead = odds, evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd, head = not isOdd, head.next
        evens.next, odds.next = None, evensHead.next
        return oddsHead.next
