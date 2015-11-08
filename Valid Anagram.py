class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        sets = [0]*26
        sett = [0]*26
        
        for char in s:
            sets[ord(char)-ord('a')]+=1
        
        for char in t:
            sett[ord(char)-ord('a')]+=1
            
        return sets == sett