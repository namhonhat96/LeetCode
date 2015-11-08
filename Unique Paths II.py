class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        if not obstacleGrid:
            return 0
            
        uniquepath = [[-1 for x in range(len(obstacleGrid[0]))] for x in range(len(obstacleGrid))]
        
        return self.findpath(0, 0, obstacleGrid, uniquepath)
        
        
    def findpath(self, m, n,obstacleGrid, uniquepath):
        a  = uniquepath[m][n]
        if a!=-1:
            return a
        if obstacleGrid[m][n]==1:
            uniquepath[m][n] =0
            return 0
        
        if m == len(obstacleGrid)-1:
            for j in range(n, len(obstacleGrid[0])):
                if obstacleGrid[m][j]==1:
                    uniquepath[m][n]=0
                    return 0
            uniquepath[m][n]=1
            return 1
        
        if n ==len(obstacleGrid[0])-1:
            for i in range(m, len(obstacleGrid)):
                if obstacleGrid[i][n]==1:
                    uniquepath[m][n]=0
                    return 0
            uniquepath[m][n]=1
            return 1
            
        a = self.findpath(m+1, n, obstacleGrid, uniquepath)
        b = self.findpath(m, n+1, obstacleGrid, uniquepath)
        c = a+b
        uniquepath[m][n]=c
        return c
        S