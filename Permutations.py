class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums)==1:
            return [nums]
        mylist = []
        for i in range(len(nums)):
            output = [nums[i]]
            newnums = nums[0:i]+nums[i+1:]
            temp= self.permute(newnums)
            for item in temp:
                mylist.append(output+item)
        return mylist