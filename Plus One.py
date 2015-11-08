class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pointer = len(digits)-1
        
        flag = 1
        for i in range(len(digits)):
            if digits[i]!=9:
                flag = 0
                break
        if flag ==1:
            digits.append(0)
            digits[0]=1
            for i in range(1, len(digits)):
                digits[i]=0
            return digits
                
        
        while digits[pointer] == 9:
            digits[pointer]=0
            pointer -=1
        digits[pointer]+=1
        
        return digits