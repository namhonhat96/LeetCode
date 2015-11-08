# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
            
        l = ListNode(0)
        first = l
        first.next = head
        second = first.next.next
        while second:
            first.next.next = second.next
            second.next = first.next
            first.next = second
            
            first = second.next
            if first.next:
                second = first.next.next
            else:
                return l.next
        return l.next