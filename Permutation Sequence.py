class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        mylist = [i for i in range(1, n+1)]
        output = ""
        while k>0:
            if k==1:
                output+="".join(str(i) for i in mylist)
                return output
            num=(k-1)/self.fact(n-1)
            output += str(mylist[num])
            mylist = mylist[:num]+mylist[num+1:]
            k = k-(num*self.fact(n-1))
            n = n-1
        return output
    def fact(self, n):
        output = 1
        for i in range(1, n+1):
            output*=i
        return output