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
        l = ListNode(0)
        l.next = head    
    
        slow, fast = l, l
        p = n
        while p>0:
            fast = fast.next
            p-=1
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return l.next
        
                
            
            
        