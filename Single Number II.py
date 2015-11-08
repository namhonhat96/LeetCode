class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return nums[0]
        bitcount = [0]*32
        
        for num in nums:
            for i in range(32):
                if num&(1<<i): ####the ith bit is 1
                    bitcount[i]+=1
                    
                    
                    
        exept = 0
        if bitcount[31]%3 != 0: ###negative
            for i in range(31):
                if bitcount[i]%3 ==0:
                    exept +=1<<i
            exept = -(exept+1)
        
        else:
            for i in range(31):
                if bitcount[i]%3 != 0:
                    exept += 1<<i
    
        return exept
        