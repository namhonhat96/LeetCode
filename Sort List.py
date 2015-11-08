# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        return self.msort(head)
        
    def msort(self, head):
        if not head.next:
            return head
        
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        head1 = head
        
        firstpart = self.msort(head1)
        secondpart = self.msort(head2)
        head = self.merge(firstpart, secondpart)
        print head.val
        return head
        
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        
        head = ListNode(0)
        temp = head
        while head1 and head2:
            if head1.val<=head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        if head1:
            temp.next = head1
        elif head2:
            temp.next = head2
        # print head.val, head.next.val
        return head.next
            
            