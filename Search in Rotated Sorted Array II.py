class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
            
        if target<nums[0]:
            if target>nums[-1]:
                return False
            elif target==nums[-1]:
                return True
            else: #target<nums[-1]
                for i in range(len(nums)-2, -1, -1):
                    if target<nums[i] and nums[i]<nums[i+1]:
                        continue
                    if target==nums[i]:
                        return True
                return False
        elif target>nums[0]:
            for i in range(1, len(nums)):
                if target==nums[i]:
                    return True
                elif target<nums[i]:
                    return False
                elif target>nums[i]:
                    if nums[i]>nums[i-1]:
                        continue
            return False
        else:
            return True
                
            