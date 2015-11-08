class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        l = 0
        t = len(s)-1
        s = s.lower()
        while l<t:
            while l<t and not s[l].isalnum():
                l+=1
            while l<t and not s[t].isalnum():
                t-=1
            
            if s[l]!=s[t]:
                return False
            l+=1
            t-=1
        return True