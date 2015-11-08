class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while True:
            if 2**i <n:
                i+=1
                continue
            if 2**i ==n:
                return True
            if 2**i >n:
                break
        return False