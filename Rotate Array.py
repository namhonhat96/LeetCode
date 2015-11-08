class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k= k%len(nums)
        if k==0:
            return
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, 0, len(nums)-1)
        
        return
        
    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return