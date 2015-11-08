class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return n
    
        temp = bin(n)
        temp = temp[2:]
        
        addigit = 32-len(temp)
        zeros = '0'*addigit
        
        temp = zeros+temp
        
        temp = temp[::-1]
        
        return int(temp,2)