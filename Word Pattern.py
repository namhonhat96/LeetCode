class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        mydict = {} ## sotres the word
        
        p = str.split()
        if len(p)!= len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mydict:
                if mydict[pattern[i]] == p[i]:
                    continue
                else:
                    return False
            else:
                j = 0
                ending = 0
                mydict[pattern[i]] = p[i]
                for num in mydict:
                    if num != pattern[i] and mydict[num]==mydict[pattern[i]]:
                        return False
        return True