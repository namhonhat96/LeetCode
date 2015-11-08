# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        i = 1
        temp = head
        while temp.next:
            temp = temp.next
            i+=1
        k = k%i
        
        l = ListNode(0)
        l.next = head
        for i in range(k):
            p = l
            while p.next.next:
                p = p.next
            l.next = p.next
            p.next = l.next.next
            l.next.next = head
            head = l.next
        return l.next
            
            