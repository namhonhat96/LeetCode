class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        if x <0:
            negative = -1
            x = x*(-1)
        
        if x <10:
            return x*negative
        
        while x %10 ==0:
            x = x/10
            
        temp = []
        while x>0:
            digits1 = self.digits(x)
            first = x/(10**(digits1-1))
            temp.append(first)
            x = x%(10**(self.digits(x)-1))
            digits2 = self.digits(x)
            zeros = digits1 - digits2 -1
            if zeros>0:
                while zeros:
                    temp.append(0)
                    zeros -=1
        
        temp.reverse()
        output = 0
        for i in range(len(temp)):
            output += temp[i]*(10**(len(temp)-i -1))
        
        output = negative*output
        if abs(output)> (2**31):
            return 0
        return output
        
        
    def digits(self, x):
        counter = 1
        while x>=10:
            x= x/10
            counter+=1
        return counter
        