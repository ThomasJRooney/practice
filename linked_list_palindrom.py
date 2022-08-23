# Given the head of a singly linked list, return true if it is a palindrome.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        if l == l[::-1]:
            return True
        return False
