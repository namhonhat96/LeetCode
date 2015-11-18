class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
            
        mylist = [0 for i in range(len(nums))]
        mylist[-1], mylist[-2]=nums[-1], nums[-2]
        
        for i in range(len(nums)-3, -1, -1):
            mylist[i] = max(mylist[i+2] if i+2 <= len(nums)-1 else 0, mylist[i+3] if i+3 <=len(nums)-1 else 0)+ nums[i]
            print i, mylist[i]    
        return max(mylist[0], mylist[1])
        
        