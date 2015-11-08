class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
            
        mylist = [i for i in mydict]
        mylist.sort()
        # print mylist
        output = []
        for num in mylist:
            lenth = 0
            if output:
                lenth = len(output)
            for i in range(1, mydict[num]+1):
                output.append([num]*i)
                for j in range(lenth):
                    output.append(output[j]+[num]*i)
        output.append([])    
        return output
       
            