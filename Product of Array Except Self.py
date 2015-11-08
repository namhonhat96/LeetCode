class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1]*n
        
        ##first scan
        i=1
        while i <n:
           result[i]=result[i-1]*nums[i-1]
           i+=1
           
        ##second scan
        temp=1
        i = n-2
        while i>=0:
            temp *= nums[i+1]
            result[i] = result[i]* temp
            i-=1
        return result
            
        
        