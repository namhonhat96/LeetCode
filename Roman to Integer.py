class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, '0':0}
        
        return sum([romanDict[c] if romanDict[c]>=romanDict[d] else romanDict[c]*-1 for c, d in zip(s, (s+'0')[1:])])