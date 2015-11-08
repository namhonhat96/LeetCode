class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        mydict = {}
        for i in nums:
            if i not in mydict:
                mydict[i]=1
            else:
                mydict[i]+=1
        return self.permute(mydict)
        
    def permute(self, mydict):
        result = []
        for num in mydict:
            if mydict[num]<=0:
                continue
            else:
                temp = dict(mydict)
                temp[num]-= 1
                output=self.permute(temp)
                if not output:
                    result.append([num])
                else:
                    for i in output:
                        result.append([num]+i)
        return result