class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
            
        if target<nums[0]:
            if target>nums[-1]:
                return -1
            elif target==nums[-1]:
                return len(nums)-1
            else: #target<nums[-1]
                for i in range(len(nums)-2, -1, -1):
                    if target<nums[i] and nums[i]<nums[i+1]:
                        continue
                    if target<nums[i] and nums[i]>nums[i+1]:
                        return -1
                    if target==nums[i]:
                        return i
                    if target>nums[i]:
                        return -1
                return -1
        elif target>nums[0]:
            for i in range(1, len(nums)):
                if target==nums[i]:
                    return i
                elif target<nums[i]:
                    return -1
                elif target>nums[i]:
                    if nums[i]>nums[i-1]:
                        continue
                    else:
                        return -1
            return -1
        else:
            return 0
                
            
            