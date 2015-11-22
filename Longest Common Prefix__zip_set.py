class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mylist = zip(*strs)
        output = ""
        for i in mylist:
            if len(set(i))>1:
                break
            output+=i[0]
        return output
            