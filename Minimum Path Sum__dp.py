class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        mat = [[0]*(n) for i in range(m)]
        mat[0][0] = grid[0][0]
        for j in range(1, n):
            mat[0][j]= mat[0][j-1]+grid[0][j]
        for i in range(1, m):
            mat[i][0]=mat[i-1][0]+grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j]=min(mat[i-1][j], mat[i][j-1])+grid[i][j]
        
        return mat[-1][-1]