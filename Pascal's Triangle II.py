class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = [0]*(rowIndex+1)
        for i in range(len(output)):
            output[i]=self.Combination(rowIndex, i)
        return output
    
    def Combination(self, i, j):
        result = 1
        for temp in range(i, i-j, -1):
            result *= temp
        factorial = 1
        for temp in range(1, j+1):
            factorial*=temp
            
        result = result/factorial
        return result