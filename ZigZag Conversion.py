class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        
        rows = ['']*numRows
        base = 2*numRows - 2
        for i, item in enumerate(s):
            if i%base<numRows:
                rows[i%base]+=item
            else:
                rows[base-i%base]+=item
        
        return "".join(rows)