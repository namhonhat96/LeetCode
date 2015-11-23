# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root or not root.left:
            return
            
        p = root
        while p.left:
            p.left.next = p.right
            q  = p
            p = p.left
            while q.next:
                q.right.next = q.next.left
                q = q.next
                q.left.next = q.right
        return
                   