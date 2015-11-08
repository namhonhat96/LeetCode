# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newlist = ListNode(0)
        newlist.next = head
        pointer = newlist
        while pointer and pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
                continue;
            pointer = pointer.next
        return newlist.next