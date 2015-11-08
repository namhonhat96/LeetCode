class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        uniquepath = [[-1 for x in range(n)] for x in range(m)]
        if m == 0 or m==0:
            return 0
        return self.paths(0, 0, uniquepath)
        
    def paths(self, m, n, uniquepath):
        a = uniquepath[m][n] 
        if a != -1:
            return a
            
        if m == len(uniquepath)-1 or n == len(uniquepath[0])-1:
            return 1
        
        a = self.paths(m+1, n, uniquepath)
        b = self.paths(m, n+1, uniquepath)
        c = a + b
        uniquepath[m][n]=c
        return c