class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
            
        first = 1
        second = 0
        temp = min(nums)-1
        while first <len(nums):
            if nums[first] == nums[first-1] or nums[first]==temp:
                first+=1
                continue
            else:
                temp = nums[first]
                second +=1
                nums[second], nums[first]=nums[first], nums[second]
                first+=1
        return second+1