# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        while head and head.val in nums:
            head = head.next
        if not head:
            return None

        prev = head
        node = head.next
        while node:
            if node.val in nums:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head
