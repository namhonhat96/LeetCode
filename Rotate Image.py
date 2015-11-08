class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n ==1:
            return
        i = 0
        while 2*(i+1) <= n:
            for pointer in range(i, n-i-1):
                print i, pointer
                temp = matrix[i][pointer]
                matrix[pointer][n-1-i], temp = temp, matrix[pointer][n-1-i]
                matrix[n-i-1][n-pointer-1], temp = temp, matrix[n-i-1][n-pointer-1]
                matrix[n-pointer-1][i], temp = temp, matrix[n-1-pointer][i]
                matrix[i][pointer] = temp
            i+=1
        return