class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        big = set()
        
        for i in xrange(9):
            for j in xrange(9):
                cur = board[i][j]
                if cur != '.':
                    if (i,cur) in big or (cur, j) in big or (i/3, j/3, cur) in big:
                        return False
                    else:
                        big.add((i,cur))
                        big.add((cur,j))
                        big.add((i/3,j/3,cur))
        return True