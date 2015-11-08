class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
            
        
        s = 0
        e = len(matrix)
        while (s<=e):
            mid = (s+e)/2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                e = mid-1
                continue
            elif matrix[mid][0]<target:
                s = mid+1 ##change here
                continue
            
        row = e
        
            