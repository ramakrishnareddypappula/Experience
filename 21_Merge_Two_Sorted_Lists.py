# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = []
        while l1:
            output.append(l1.val)
            l1 = l1.next
        while l2:
            output.append(l2.val)
            l2 = l2.next
        output.sort()
        head = None
        temp = None
        for each in output:
            if head is None:
                head = ListNode(each)
                temp = head
            else:
                new_node = ListNode(each)
                temp.next = new_node
                temp = new_node
        return head