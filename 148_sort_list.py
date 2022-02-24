# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Top down merge sort: Divide and conquer strategy: Divide the list into sublists of equal sizes. Repeatedly solve subproblem independently and combine result to form original pronblem.
        # Time = O(n log n)) when n is number of nodes in linked list.
        # Space = O(log n) when n is number nodes in linked list. Since problem is recursive we need additional space to store the recursive call stack. Max depth is Log n.  
        if (head is None) or (head.next is None):
            return head  # Warning: Use "is None" or "is not None" instead of "not head".
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        dummyhead = ListNode()
        tail = dummyhead
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        tail.next = list1 if list1 is not None else list2
        return dummyhead.next
    
    def get_mid(self, head):
        midp = None
        while (head is not None) and (head.next is not None):
            midp = head if midp is None else midp.next
            head = head.next.next
        mid = midp.next
        midp.next = None
        return mid
