class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowchecked = []
        colchecked = []
        squarechecked = []
        for r in range(9):
            for c in range(9):
                square = (r/3)*3+c/3
                if board[r][c]!= '.':
                    if self.checkrow(r, rowchecked, board) and self.checkcol(c, colchecked, board) and self.checksquare(square, squarechecked, board):
                        continue
                    return False
        return True
        
    def checkrow(self, row, rowchecked, board):
        if row in rowchecked:
            return True
        temp = board[row][:]
        temp.sort()
        for i in range(8):
            if temp[i+1] != '.'and temp[i+1]==temp[i]:
                return False
        rowchecked.append(row)
        return True
        
    def checkcol(self, col, colchecked, board):
        if col in colchecked:
            return True
        temp = []
        for i in range(9):
            if board[i][col] == '.':
                continue
            elif board[i][col] not in temp:
                temp.append(board[i][col])
            else:
                return False
        colchecked.append(col)
        return True
    
    def checksquare(self, square, squarechecked, board):
        if square in squarechecked:
            return True
        temp = []
        for i in range(3):
            for j in range(3):
                print (square/3)*3+i, 3*(square%3)+j
                if board[(square/3)*3+i][3*(square%3)+j] == '.':
                    continue
                elif board[(square/3)*3+i][3*(square%3)+j] in temp:
                    return False
                temp.append(board[(square/3)*3+i][3*(square%3)+j])

        squarechecked.append(square)
        return True
        