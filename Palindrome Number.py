class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x<10:
            return True
        
        if x%10 == 0:
            return False
        
        digits1=self.calclog(x)
        
        firstdigit = x/(10**digits1)
        
        lastdigit = x%10
        if firstdigit != lastdigit:
            return False
        
        digits2 = self.calclog(x%(10**digits1))
        
        if((x%(10**digits1))-lastdigit)==0:
            return True
        if ((x%(10**digits1))-lastdigit)%(10**(digits1-digits2))!=0:
            return False
            
        return self.isPalindrome(((x%(10**digits1))-lastdigit)/(10**(digits1-digits2)))   
            
    def calclog(self, num):
        counter = 0
        while num>=10:
            num = num/10
            counter +=1
        return counter