class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<=2:
            return len(nums)
        
        slow, fast = 0, 1
        counter = 1
        while fast <= len(nums)-1:
            if nums[fast]==nums[slow] and counter==1:
                slow+=1
                nums[slow]=nums[fast]
                counter+=1
            elif nums[fast] !=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
                counter=1
            fast+=1
            
        return slow+1