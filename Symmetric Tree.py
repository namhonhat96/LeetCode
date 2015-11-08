# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = root.left
        right = root.right
        return self.symmetric(left, right)
        
    def symmetric(self, leftroot, rightroot):
        if not leftroot:
            if not rightroot:
                return True
            return False
        if not rightroot:
            return False
        
        if leftroot.val != rightroot.val:
            return False
        
        if self.symmetric(leftroot.left, rightroot.right) and self.symmetric(leftroot.right, rightroot.left):
            return True
        return False