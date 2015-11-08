class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        
        if not nums:
            return []
            
        if len(nums)==1:
            output.append(str(nums[0]))
            return output
            
        start = 0
        end = 1
        while end <len(nums):
            if nums[end]==nums[end-1]+1:
                end+=1
            else:
                if end == start+1:
                    output.append(str(nums[start]))
                else:
                    output.append(str(nums[start])+'->'+str(nums[end-1]))
                start=end
                end+=1
        if end == start+1:
            output.append(str(nums[start]))
        else:
            output.append(str(nums[start])+'->'+str(nums[end-1]))
        return output
            