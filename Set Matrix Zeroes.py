class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        mydict = {"row":[], "col":[]}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    mydict["row"].append(i)
                    mydict["col"].append(j)
                    
        mydict["row"]=list(set(mydict["row"]))
        mydict["col"]=list(set(mydict["col"]))
        
        for i in range(len(matrix)):
            if i in mydict["row"]:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
            else:
                for j in mydict["col"]:
                    matrix[i][j]=0
        return 