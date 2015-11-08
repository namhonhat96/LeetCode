class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rawarea= self.calcarea(A, B, C, D)+self.calcarea(E, F, G, H)

        ##no overlapping
        if (A>=G) or (C<=E) or (B>=H) or (D<=F):
            return rawarea
    
        ##overlapping
        col1 = sorted([A, C, E, G])[1]
        col2 =sorted([A, C, E, G])[2]
        row1 = sorted([B,D,F,H])[1]
        row2 =sorted([B,D,F,H])[2]
        overlaparea = self.calcarea(col1,row1,col2,row2)
        return rawarea-overlaparea
        
        
    def calcarea(self, A, B, C, D):
        return abs(C-A)*abs(D-B)