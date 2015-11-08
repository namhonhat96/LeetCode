class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
            
        output = [[0 for i in range(n)] for i in range(n)]
        direction = 0
        posi=0
        posj=-1
        for i in range(1, n**2+1):
            if direction%4 == 0:
                posj+=1
                if posj+1>=n or output[posi][posj+1] >0:
                    direction+=1
            elif direction%4 ==1:
                posi+=1
                if posi+1>=n or output[posi+1][posj]>0:
                    direction+=1
            elif direction%4 ==2:
                posj-=1
                if posj-1<0 or output[posi][posj-1]>0:
                    direction+=1
            else:
                posi-=1
                print posi, posi-1, posj,output[posi-1][posj]
                if output[posi-1][posj]>0:
                    direction+=1
            output[posi][posj]=i
            print i, direction%4
        return output
                
                
                
