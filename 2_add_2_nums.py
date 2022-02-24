# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        out = ListNode()
        temp = out
        while (l1 is not None) or (l2 is not None):
            p = l1.val if l1 is not None else 0
            q = l2.val if l2 is not None else 0
            sum1 = p + q + carry
            carry = sum1 // 10
            sum1 = sum1 % 10
            out.next = ListNode(sum1)
            out = out.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            out.next = ListNode(carry)
        return temp.next
