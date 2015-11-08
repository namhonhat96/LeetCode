class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
            
        col = len(board[0])
        row = len(board)
        print len(word)
        if col * row < len(word):
            return False
        
        visited = [[0 for x in xrange(col)] for y in xrange(row)]  
        # print visited
        
        for i in range(row):
            for j in range(col):
                if self.search(board, word, i, j, visited):
                    return True
        return False
        
    def search(self, board, word, row, col, visited):
        if not word:
            return True
        
        if row <0 or col <0 or row >= len(board) or col >= len(board[0]):
            return False
        
        if visited[row][col]==1 or board[row][col]!=word[0]:
            return False
            
        visited[row][col]=1    
        
        res = self.search(board, word[1:], row+1, col, visited) or self.search(board, word[1:], row-1, col, visited) or self.search(board, word[1:], row, col+1, visited) or self.search(board, word[1:], row, col-1, visited)
        visited[row][col]=0
        
        return res
                    