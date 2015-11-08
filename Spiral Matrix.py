class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return[]
        
        m=len(matrix)
        n = len(matrix[0])
        temp = [[1 for i in range(n)] for i in range(m)]
        direction = 0
        posi = 0
        posj = -1
        output = []
        for i in range(m*n):
            if direction%4 ==0:
                posj+=1
                if posj+1 >= len(matrix[0]) or temp[posi][posj+1]==0:
                    direction+=1
            elif direction%4 ==1:
                posi+=1
                if posi+1 >=len(matrix) or temp[posi+1][posj]==0:
                    direction+=1
            elif direction%4==2:
                posj-=1
                if posj-1<0 or temp[posi][posj-1]==0:
                    direction+=1
            elif direction%4==3:
                posi-=1
                print temp, posi, posj,temp[posi-1][posj-1]
                if temp[posi-1][posj]==0:
                    direction+=1
            else:
                print "error"
            temp[posi][posj]=0
            output.append(matrix[posi][posj])
        return output
        