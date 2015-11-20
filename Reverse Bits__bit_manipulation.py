class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in xrange(32):
            ans = ans | (n&1)
            n = n>> 1
            ans = ans << 1
        ans = ans>>1
        return ans