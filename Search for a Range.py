class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
            
        if len(nums)==1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]
            
        if nums[0]>target or nums[-1]<target:
            return [-1, -1]
         
        lenth = len(nums)
        p = 0
        while True:
            if lenth == 0:
                return [-1, -1]
            if lenth == 1:
                if nums[p]!= target:
                    return [-1, -1]
            half = lenth/2
            if nums[p+half]==target:
                i, j = p+half, p+half
                while i-1>=0 and nums[i-1]==target:
                    i-=1
                start = i
                while j+1<len(nums) and nums[j+1]==target:
                    j+=1
                end = j
                return [i, j]
            if nums[p+half]<target:
                p = p+half
                lenth = lenth - half
                continue
            else:
                lenth = half
                continue
            