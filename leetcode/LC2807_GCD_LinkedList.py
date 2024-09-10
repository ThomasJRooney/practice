class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if head.next == None:
            return head
        def get_gcd(num1, num2):
            for i in range(min(num1, num2), 0, -1):
                if num1 % i == 0 and num2 % i == 0:
                    return i
            return 1

        cur = head
        nex = cur.next
        while cur and nex:
            gcd = get_gcd(cur.val, nex.val)
            new = ListNode(val=gcd)
            tmp = cur
            cur = nex
            nex = nex.next
            tmp.next = new
            new.next = cur
        return head
