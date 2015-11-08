class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        
        if numRows == 0:
            return output
            
        counter = 0
        output.append([1])
        counter+=1
        while counter <numRows:
            temp = [0]*(counter+1)
            temp[0]=1
            for i in range(1, counter):
                temp[i]=output[counter-1][i-1]+output[counter-1][i]
            temp[counter] = 1
            output.append(temp)
            counter+=1
        
        return output
            
            
            