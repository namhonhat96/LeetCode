class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        if len(nums)==2:
            return nums[0], nums[1]
            
        xor = reduce(lambda x, y: x^y, nums)
        
        for i in range(32):
            if xor & 1<<i:
                xor = 1<<i
                break
        
        a = 0
        b = 0
        for num in nums:
            if num & (1<<i):
                a ^= num
            else:
                b ^=num
        
        return [a, b]