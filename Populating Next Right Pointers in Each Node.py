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
        if not root:
            return
        if not root.left:
            root.next = None
            return
        
        q = []
        q.append((root, 0))
        pointer = 0
        while pointer<len(q):
            if q[pointer][0].left:
                q.append((q[pointer][0].left,q[pointer][1]+1))
                q.append((q[pointer][0].right,q[pointer][1]+1))
            pointer+=1
            
        
        for counter in range(0, len(q)-1):
            node, level = q[counter][0], q[counter][1]
            if level == q[counter+1][1]:
                node.next = q[counter+1][0]
            else:
                node.next = None
        q[-1][0].next = None    
        
        return
                