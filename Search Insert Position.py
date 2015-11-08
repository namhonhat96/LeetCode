class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None
            
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
        
        return len(nums)