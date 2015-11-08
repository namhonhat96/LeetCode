class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {')':'(', '}':'{', ']':'['}
        if not s:
            return True
        if len(s)%2 ==1:
            return False
        i=0
        while s[i] not in mydict:
            i+=1
            if i> (len(s)/2):
                return False
        if i==0 or mydict[s[i]]!=s[i-1]:
            return False
        if i>=2:
            temp = s[:(i-1)] +s[(i+1):]
        else:
            temp = s[(i+1):]
        s = temp
        return self.isValid(s)