# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        outsum = 0
        mylist, outsum = self.sumtree(0, root)
        return outsum
        
    def sumtree(self, outsum, root):
        output = []
        if not root.right and not root.left:
            outsum += root.val
            return ([1], outsum)
        if root.left:
            digits, outsum = self.sumtree(outsum, root.left)
            for i in digits:
                outsum+=root.val*10**(i)
                output.append(i+1)
        if root.right:
            digits, outsum = self.sumtree(outsum, root.right)
            for i in digits:
                outsum+=root.val*10**(i)
                output.append(i+1)
        return (output, outsum)
        