# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
            
        counter = 0
        pointer = head
        
        while pointer:
            pointer = pointer.next
            counter+=1
            
        total = counter ##how many nodes in total
        n1 = total -n ##head counter =0
        
        temphead = ListNode(0)
        temphead.next = head
        pointer = temphead
        counter = 0
        while counter != n1:
            pointer = pointer.next
            counter+=1
            
        pointer.next =pointer.next.next
        
        return temphead.next
        
        