class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
            
            
        count0 = 0
        count1 = 0
        count2 = 0
        for i in nums:
            if i == 0:
                count0+=1
            elif i == 1:
                count1+=1
            else:
                count2+=1
        for i in range(len(nums)):
            if i <count0:
                nums[i]=0
            elif i <(count0+count1):
                nums[i]=1
            else:
                nums[i]=2
        return
        