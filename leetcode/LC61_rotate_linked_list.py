# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        lastNode, length = head, 1
        while lastNode.next:
            lastNode = lastNode.next
            length += 1
        k %= length
        lastNode.next = head
        tmp = head
        for _ in range(length - k - 1):
            tmp = tmp.next
        answer = tmp.next
        tmp.next = None
        return answer