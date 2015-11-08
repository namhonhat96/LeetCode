class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 1
        list = []
        new = 1
        list.append(new)
        a, b, c = 0, 0, 0
        
        while count <n:
            newa = 2*list[a]
            newb = 3*list[b]
            newc = 5*list[c]
            new = min(newa, newb, newc)
            if new == newa:
                a+=1
            if new == newb:
                b+=1
            if new == newc:
                c+=1
            list.append(new)
            count+=1
        return new
                
            
        