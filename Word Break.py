class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        if s in wordDict:
            return True
        
        breakable = [0]*(len(s)+1)
        breakable[0]=1
        

            
        for i in range(1, len(s)+1):
            for k in range(i+1):  
                if breakable[k] and (s[k:i] in wordDict):
                    breakable[i] = 1
            print breakable
        
        return bool(breakable[-1])
        